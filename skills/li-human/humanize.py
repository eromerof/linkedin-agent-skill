#!/usr/bin/env python3
"""
humanize.py - quita la huella de máquina de un borrador en español.

Tres pasadas, en este orden:

  1. INVISIBLES  borra o normaliza los caracteres que un teclado humano nunca
                 produce: espacios de anchura cero, unidores de palabra,
                 guiones blandos, BOM, caracteres de etiqueta Unicode,
                 espacios duros y finos. Sobreviven al copiar y pegar y son la
                 señal más mecánica de cualquier texto generado.
  2. TIPOGRAFÍA  raya (—) -> coma, semirraya -> guion, comillas curvas y
                 angulares («») -> rectas, elipsis -> tres puntos,
                 viñeta -> guion. Los signos ¿ y ¡ no se tocan nunca.
  3. LÉXICO      sustituye el léxico de relleno de slop.json por palabras
                 llanas, respetando mayúsculas y sin tocar las URL. Las
                 entradas con "replace": null solo se señalan: son palabras
                 que a veces están bien usadas y necesitan criterio.

Los patrones estructurales ("no es solo X, es Y", tríadas, muros de
hashtags, meses en mayúscula) se SEÑALAN, nunca se reescriben solos: cambiar
la forma de una frase exige criterio, y eso es trabajo del modelo, no de una
expresión regular.

Uso
  python3 humanize.py borrador.txt
  python3 humanize.py borrador.txt --report
  pbpaste | python3 humanize.py - --report
  python3 humanize.py borrador.txt --json
  python3 humanize.py borrador.txt -o limpio.txt
"""

import argparse
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

URL_RE = re.compile(r"https?://\S+|www\.\S+|\S+@\S+\.\S+")
SENT_RE = re.compile(r"(?:[^.!?…\n]|(?<=\d)\.(?=\d))+[.!?…]*")
DELETED = "\x01"


def load_lexicon(path=LEX):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _cp(spec):
    """'U+200B' -> 0x200b;  'U+E0000-U+E007F' -> (inicio, fin)."""
    if "-" in spec:
        a, b = spec.split("-")
        return (int(a[2:], 16), int(b[2:], 16))
    return int(spec[2:], 16)


def lex_pattern(find):
    # \b does not work next to ¿ or ¡, so use explicit word-character guards.
    body = re.escape(find).replace(r"\ ", r"\s+")
    return re.compile(r"(?<!\w)" + body + r"(?!\w)", re.IGNORECASE)


def protect_urls(text):
    """Cambia las URL por marcadores para que ninguna pasada reescriba un enlace."""
    found = []

    def stash(m):
        found.append(m.group(0))
        return f"\x00URL{len(found) - 1}\x00"

    return URL_RE.sub(stash, text), found


def restore_urls(text, found):
    for i, url in enumerate(found):
        text = text.replace(f"\x00URL{i}\x00", url)
    return text


def pass_invisible(text, lex):
    """Borra o convierte en espacio los caracteres invisibles. Devuelve (texto, cambios)."""
    hits = []
    for entry in lex["invisible"]:
        cp = _cp(entry["cp"])
        if isinstance(cp, tuple):
            pattern = "[" + re.escape(chr(cp[0])) + "-" + re.escape(chr(cp[1])) + "]"
        else:
            pattern = re.escape(chr(cp))
        n = len(re.findall(pattern, text))
        if n:
            hits.append({"name": entry["cp"] + " " + entry["name"], "count": n,
                         "action": entry["action"]})
            text = re.sub(pattern, "" if entry["action"] == "delete" else " ", text)
    # Any remaining Cf (format) character is invisible by definition.
    stray = [c for c in text if unicodedata.category(c) == "Cf"]
    if stray:
        hits.append({"name": "otros caracteres de formato invisibles", "count": len(stray),
                     "action": "delete"})
        text = "".join(c for c in text if unicodedata.category(c) != "Cf")
    return text, hits


def pass_typographic(text, lex):
    hits = []
    for entry in lex["typographic"]:
        ch = entry["from"]
        n = text.count(ch)
        if not n:
            continue
        hits.append({"name": f"{ch} {entry['name']}", "count": n,
                     "to": entry["to"].strip() or "(espacio)"})
        if ch == "—":
            # " palabra — palabra ", "palabra —inciso— palabra" and "palabra—palabra"
            # all collapse to a comma and a space.
            text = re.sub(r"\s*—\s*", ", ", text)
        elif ch == "–":
            text = re.sub(r"\s*–\s*(?=\d)", "-", text)      # 5–10  -> 5-10
            text = re.sub(r"\s+–\s+", ", ", text)            # used as a raya
            text = text.replace("–", "-")
        else:
            text = text.replace(ch, entry["to"])
    # A comma inserted before existing punctuation reads wrong.
    text = re.sub(r",\s*([,.;:!?])", r"\1", text)
    text = re.sub(r",\s*\n", "\n", text)
    text = re.sub(r"(?m)^[ \t]*,[ \t]*", "", text)
    return text, hits


def _match_case(src, repl):
    if not repl:
        return repl
    if src.isupper() and len(src) > 1:
        return repl.upper()
    if src[0].isupper():
        return repl[0].upper() + repl[1:]
    return repl


def pass_lexical(text, lex):
    """Sustituye palabras y frases de relleno. Las más largas primero, para que ganen las frases."""
    hits, review = [], []
    entries = sorted(lex["phrases"] + lex["words"],
                     key=lambda e: len(e["find"]), reverse=True)
    for entry in entries:
        find, repl = entry["find"], entry["replace"]
        pattern = lex_pattern(find)
        found = pattern.findall(text)
        if not found:
            continue
        if repl is None:
            review.append({"find": find, "count": len(found), "family": entry["family"],
                           "note": entry.get("note", "")})
            continue
        hits.append({"find": find, "replace": repl or "(borrado)",
                     "count": len(found), "family": entry["family"]})
        text = pattern.sub(lambda m: _match_case(m.group(0), repl) if repl else DELETED, text)
    # A deletion at the start of a sentence leaves it starting in lowercase:
    # "Cabe destacar que el equipo..." -> "El equipo...".
    text = re.sub(r"(?m)(^[ \t]*|[.!?][ \t]+|[¿¡])" + DELETED + r"[ \t]*[,;:]?[ \t]*(\w)",
                  lambda m: m.group(1) + m.group(2).upper(), text)
    text = text.replace(DELETED, "")
    # Clean up after deletions.
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"(?m)^[ \t]*([,.;:])[ \t]*", "", text)
    text = re.sub(r"[ \t]+([,.;:!?])", r"\1", text)
    text = re.sub(r",\s*([,.;:!?])", r"\1", text)
    text = re.sub(r"([¿¡])\s+", r"\1", text)
    text = re.sub(r"(?m)^[ \t]+$", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # A raya that became a comma, followed by a connective, leaves a splice
    # ("es clave, además, demuestra..."). Promote it to a full stop.
    text = re.sub(r",\s*(además|así que|aun así|total|al final|en el fondo)\s*,\s*",
                  lambda m: ". " + m.group(1)[0].upper() + m.group(1)[1:] + ", ", text)
    return text, hits, review


def scan_structures(text, lex):
    flags = []
    for s in lex["structures"]:
        try:
            pattern = re.compile(s["regex"], re.MULTILINE)
        except re.error:
            continue
        found = pattern.findall(text)
        if found:
            flags.append({"name": s["name"], "count": len(found), "fix": s["fix"]})
    # Sentence-length uniformity is structural too.
    lens = [len(s.split()) for s in SENT_RE.findall(text) if len(s.split()) > 2]
    if len(lens) >= 4:
        mean = sum(lens) / len(lens)
        var = sum((n - mean) ** 2 for n in lens) / len(lens)
        cv = (var ** 0.5) / mean if mean else 0
        if cv < 0.35:
            flags.append({
                "name": "Longitud de frase uniforme (variación " + f"{cv:.2f}".replace(".", ",") + ")",
                "count": len(lens),
                "fix": "Parte una frase en dos. Deja que otra se alargue. Las máquinas escriben parejo.",
            })
    return flags


def humanize(text, lex):
    text, urls = protect_urls(text)
    text, inv = pass_invisible(text, lex)
    text, typo = pass_typographic(text, lex)
    text, lexi, review = pass_lexical(text, lex)
    text = restore_urls(text, urls)
    return text.strip() + "\n", {
        "invisible": inv,
        "typographic": typo,
        "lexical": lexi,
        "review": review,
        "structures": scan_structures(text, lex),
    }


def render_report(report, out=sys.stderr):
    def head(title):
        print(f"\n{title}\n" + "-" * len(title), file=out)

    total = sum(h["count"] for h in report["invisible"]) \
        + sum(h["count"] for h in report["typographic"]) \
        + sum(h["count"] for h in report["lexical"])

    head("INFORME DEL HUMANIZADOR")
    print(f"{total} artefactos de máquina eliminados, "
          f"{len(report['review'])} términos para revisar a mano, "
          f"{len(report['structures'])} patrones estructurales señalados", file=out)

    if report["invisible"]:
        head("1. CARACTERES INVISIBLES")
        for h in report["invisible"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['action']}", file=out)
    if report["typographic"]:
        head("2. TIPOGRAFÍA")
        for h in report["typographic"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['to']}", file=out)
    if report["lexical"]:
        head("3. LÉXICO DE RELLENO")
        for h in report["lexical"]:
            print(f"  {h['count']:>3}x  {h['find']}  -> {h['replace']}   [{h['family']}]", file=out)
    if report["review"]:
        head("4. REVISAR A MANO  (a veces están bien usados; decide tú)")
        for h in report["review"]:
            note = f"   {h['note']}" if h["note"] else ""
            print(f"  {h['count']:>3}x  {h['find']}   [{h['family']}]{note}", file=out)
    if report["structures"]:
        head("5. PATRONES ESTRUCTURALES  (no se arreglan solos: reescríbelos tú)")
        for h in report["structures"]:
            print(f"  {h['count']:>3}x  {h['name']}\n        {h['fix']}", file=out)
    if not any(report.values()):
        head("LIMPIO")
        print("  No hay nada que quitar.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Quita la huella de máquina de un borrador.")
    ap.add_argument("input", nargs="?", default="-", help="archivo, o - para stdin")
    ap.add_argument("-o", "--out", help="escribe aquí el texto limpio en vez de en stdout")
    ap.add_argument("--report", action="store_true", help="muestra qué ha cambiado, en stderr")
    ap.add_argument("--json", action="store_true", help="emite {text, report} en JSON")
    ap.add_argument("--lexicon", default=LEX, help="ruta a slop.json")
    args = ap.parse_args()

    if args.input == "-":
        raw = sys.stdin.read()
    else:
        with open(args.input, encoding="utf-8") as fh:
            raw = fh.read()
    lex = load_lexicon(args.lexicon)
    clean, report = humanize(raw, lex)

    if args.json:
        print(json.dumps({"text": clean, "report": report}, indent=2, ensure_ascii=False))
        return
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(clean)
        print(f"escrito {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(clean)
    if args.report:
        render_report(report)


if __name__ == "__main__":
    main()

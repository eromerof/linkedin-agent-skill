#!/usr/bin/env python3
"""
detect.py - un panel de cinco pruebas que puntúa cuánto parece escrito por una
máquina un borrador en español.

Qué es:  cinco heurísticas locales calcadas de las señales que miden los
detectores públicos de IA: variación en la longitud de las frases, concreción,
vocabulario de relleno, huella tipográfica y voz. Todo se calcula en tu
máquina, solo a partir del texto. No se sube nada.

Qué NO es:  GPTZero, Originality, Copyleaks, Winston ni Turnitin. No llama a
sus APIs y no puede prometer su veredicto. Detecta lo mismo en lo que se fijan
todos ellos, por eso arreglarlo suele mover también sus números, pero la única
afirmación honesta es la de esta línea.

Adaptado al español: el español no tiene contracciones como el inglés, así que
la prueba de VOZ mide marcadores coloquiales ("pues", "vale", "ojo"...),
primera y segunda persona y el abuso de adverbios en -mente. La de CONCRECIÓN
entiende cifras en formato español (4.200 €, 4,5 %), meses y días de la
semana.

Cada prueba devuelve una puntuación HUMANA de 0 a 100. Más alto es mejor.

Uso
  python3 detect.py borrador.txt
  pbpaste | python3 detect.py -
  python3 detect.py borrador.txt --json
  python3 detect.py antes.txt despues.txt      # comparar dos borradores
"""

import argparse
import json
import os
import re
import statistics
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

# A dot between digits (4.200) is a thousands separator, not the end of a sentence.
SENT_RE = re.compile(r"(?:[^.!?…\n]|(?<=\d)\.(?=\d))+[.!?…]*")
WORD_RE = re.compile(r"[^\W\d_]+(?:['-][^\W\d_]+)*")
NUMBERS = re.compile(r"(?<![\w.,])\d+(?:[.,]\d+)*")
PROPER = re.compile(r"(?<![.!?:]\s)(?<![¿¡\"«(])(?<!^)\b[A-ZÁÉÍÓÚÑ][a-záéíóúñü]{2,}\b",
                    re.MULTILINE)
TIME_WORDS = re.compile(
    r"(?<!\w)(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre"
    r"|octubre|noviembre|diciembre|lunes|martes|miércoles|jueves|viernes|sábado|domingo"
    r"|ayer|anteayer|anoche)(?!\w)", re.IGNORECASE)
COLLOQUIAL = re.compile(
    r"(?<!\w)(?:pues|vale|ojo|o sea|la verdad|eso sí|total|en fin|bueno|mira|oye|venga"
    r"|a ver|qué va|vamos|yo qué sé|por cierto|que conste|ni más ni menos|anda|madre mía"
    r"|uf|buah|ostras|jaja\w*|vaya|menudo|menuda|fatal|genial|un montón|tela|currar"
    r"|curro|mola|guay|flipar|flipé|liarla|lío|tontería|chorrada|pasta|gordo|gorda)(?!\w)",
    re.IGNORECASE)
PERSON = re.compile(
    r"(?<!\w)(?:yo|me|mi|mis|conmigo|nosotros|nosotras|nos|nuestro|nuestra|nuestros"
    r"|nuestras|tú|te|ti|tu|tus|contigo|vosotros|vosotras|os|vuestro|vuestra|vuestros"
    r"|vuestras|usted|ustedes)(?!\w)", re.IGNORECASE)
MENTE = re.compile(r"(?<!\w)[a-záéíóúñü]{4,}mente(?!\w)", re.IGNORECASE)
NOT_MENTE = {"mente", "demente", "clemente", "simiente", "vehemente"}


def es(n, d=1):
    """Formato decimal español: 4,5 en vez de 4.5."""
    return f"{n:.{d}f}".replace(".", ",")


def clamp(n):
    return max(0.0, min(100.0, n))


def scale(value, human, machine):
    """Lleva `value` a 0-100, donde `human` -> 100 y `machine` -> 0."""
    if human == machine:
        return 50.0
    return clamp((value - machine) / (human - machine) * 100)


def sentences(text):
    return [s.strip() for s in SENT_RE.findall(text) if len(s.split()) > 2]


def words(text):
    return WORD_RE.findall(text)


def lex_pattern(find):
    body = re.escape(find).replace(r"\ ", r"\s+")
    return re.compile(r"(?<!\w)" + body + r"(?!\w)", re.IGNORECASE)


def check_burstiness(text):
    """Los humanos varían mucho la longitud de las frases. Los modelos escriben parejo."""
    lens = [len(s.split()) for s in sentences(text)]
    if len(lens) < 4:
        return 50.0, "demasiado corto para juzgar"
    mean = statistics.mean(lens)
    cv = statistics.pstdev(lens) / mean if mean else 0
    score = scale(cv, human=0.70, machine=0.22)
    return score, f"variación {es(cv, 2)} en {len(lens)} frases (objetivo 0,55+)"


def check_specificity(text):
    """Cifras, nombres, fechas. El relleno es abstracto."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "demasiado corto para juzgar"
    per100 = 100 / len(w)
    hits = (len(NUMBERS.findall(text)) + len(set(PROPER.findall(text)))
            + len(TIME_WORDS.findall(text)))
    density = hits * per100
    score = scale(density, human=6.0, machine=0.5)
    return score, f"{hits} marcadores concretos, {es(density)} por cada 100 palabras (objetivo 4+)"


def check_slop(text, lex):
    """Densidad de vocabulario de relleno según el léxico."""
    w = words(text)
    if not w:
        return 50.0, "vacío"
    hits, found = 0, []
    for entry in lex["words"] + lex["phrases"]:
        n = len(lex_pattern(entry["find"]).findall(text))
        if n:
            hits += n
            found.append(entry["find"])
    density = hits * 100 / len(w)
    score = scale(density, human=0.0, machine=4.0)
    detail = f"{hits} términos de relleno, {es(density)} por cada 100 palabras"
    if found:
        detail += " (" + ", ".join(sorted(found)[:4]) + (", ..." if len(found) > 4 else "") + ")"
    return score, detail


def check_fingerprint(text):
    """Caracteres que un teclado de móvil no produce."""
    invisible = sum(1 for c in text if unicodedata.category(c) == "Cf")
    # The raya is correct Spanish, but nobody types it on LinkedIn. The spaced,
    # English-style " — " is the stronger machine tell.
    spaced = len(re.findall(r"\s—\s", text))
    raya = text.count("—") - spaced
    curly = sum(text.count(c) for c in "‘’“”")
    angular = sum(text.count(c) for c in "«»")
    ellip = text.count("…")
    nbsp = sum(text.count(c) for c in "\u00a0\u202f\u2009")
    total = invisible * 4 + spaced * 2 + raya + curly + angular + ellip + nbsp
    per1k = total * 1000 / max(len(text), 1)
    score = scale(per1k, human=0.0, machine=12.0)
    detail = (f"{invisible} invisibles, {spaced} raya espaciada, {raya} raya pegada, "
              f"{curly} comillas curvas, {angular} angulares, {ellip} elipsis, "
              f"{nbsp} espacio duro")
    return score, detail


def check_voice(text, lex):
    """Coloquialidad, persona, adverbios en -mente y las formas por defecto del modelo."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "demasiado corto para juzgar"
    per100 = 100 / len(w)
    colloquial = len(COLLOQUIAL.findall(text)) * per100
    person = len(PERSON.findall(text)) * per100
    mente = len([m for m in MENTE.findall(text) if m.lower() not in NOT_MENTE]) * per100
    tells = 0
    names = []
    for s in lex["structures"]:
        try:
            n = len(re.compile(s["regex"], re.MULTILINE).findall(text))
        except re.error:
            continue
        if n:
            tells += n
            names.append(s["id"])
    bullets = [len(b.split()) for b in re.findall(r"(?m)^\s*[-*•]\s+(.+)$", text)]
    uniform = (len(bullets) >= 3 and statistics.pstdev(bullets) < 1.6)
    score = (scale(colloquial, human=1.2, machine=0.0) * 0.25
             + scale(person, human=6.0, machine=1.0) * 0.30
             + scale(mente, human=0.3, machine=2.0) * 0.15
             + clamp(100 - tells * 22) * 0.30)
    if uniform:
        score -= 12
        names.append("viñetas-uniformes")
    detail = (f"{es(colloquial)} coloquialismos, {es(person)} marcas de 1.ª/2.ª persona, "
              f"{es(mente)} adverbios en -mente por cada 100 palabras, "
              f"{tells} patrón(es) estructural(es)")
    if names:
        detail += " [" + ", ".join(names[:4]) + (", ..." if len(names) > 4 else "") + "]"
    return clamp(score), detail


CHECKS = ["RITMO", "CONCRECIÓN", "RELLENO", "HUELLA", "VOZ"]


def run(text, lex):
    results = {}
    results["RITMO"] = check_burstiness(text)
    results["CONCRECIÓN"] = check_specificity(text)
    results["RELLENO"] = check_slop(text, lex)
    results["HUELLA"] = check_fingerprint(text)
    results["VOZ"] = check_voice(text, lex)
    scores = [results[c][0] for c in CHECKS]
    # The weakest check drags the verdict: a detector only needs one signal.
    overall = statistics.mean(scores) * 0.6 + min(scores) * 0.4
    verdict = "APROBADO" if overall >= 70 and min(scores) >= 55 else (
        "REVISAR" if overall >= 50 else "SOSPECHOSO")
    return results, overall, verdict


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render(results, overall, verdict, label=None, out=sys.stdout):
    title = "PANEL DE DETECCIÓN DE IA" + (f"  -  {label}" if label else "")
    print("\n" + title, file=out)
    print("=" * max(len(title), 62), file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {name:<13} {bar(score)} {es(score):>5}", file=out)
        print(f"  {'':<13} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'NOTA HUMANA':<13} {bar(overall)} {es(overall):>5}   {verdict}", file=out)
    if verdict != "APROBADO":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Señal más débil: {weakest}. Arregla eso primero.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Puntúa cuánto parece escrito por una máquina un borrador.")
    ap.add_argument("input", nargs="?", default="-", help="archivo, o - para stdin")
    ap.add_argument("compare", nargs="?", help="segundo archivo, para ver el antes y el después")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lexicon", default=LEX)
    args = ap.parse_args()

    with open(args.lexicon, encoding="utf-8") as fh:
        lex = json.load(fh)

    def read(p):
        if p == "-":
            return sys.stdin.read()
        with open(p, encoding="utf-8") as fh:
            return fh.read()

    targets = [(args.input, read(args.input))]
    if args.compare:
        targets.append((args.compare, read(args.compare)))

    payload = []
    for name, text in targets:
        results, overall, verdict = run(text, lex)
        payload.append({
            "source": name,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "human_score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if args.compare else payload[0], indent=2, ensure_ascii=False))
        return

    for (name, text), p in zip(targets, payload):
        results, overall, verdict = run(text, lex)
        render(results, overall, verdict, label=os.path.basename(name) if args.compare else None)
    if args.compare:
        a, b = payload
        delta = b["human_score"] - a["human_score"]
        print(f"  {es(a['human_score'])} {a['verdict']}  ->  "
              f"{es(b['human_score'])} {b['verdict']}   ({'+' if delta >= 0 else ''}{es(delta)})\n")

    sys.exit(0 if payload[-1]["verdict"] == "APROBADO" else 1)


if __name__ == "__main__":
    main()

---
name: li-carousel
description: >-
  Monta un documento de LinkedIn (carrusel) en español: el texto diapositiva a
  diapositiva, la portada que consigue el deslizamiento y el PDF para subir.
  Úsala cuando el usuario diga "carrusel", "documento para LinkedIn",
  "diapositivas para LinkedIn", "convierte esto en un carrusel", o tenga una
  idea en forma de lista que moriría como post de texto.
---

# li-carousel

Los carruseles son el formato con más tiempo de permanencia de LinkedIn,
porque cada deslizamiento cuenta y un scroll no. En el estudio de Metricool de
2026 (673.658 publicaciones) el carrusel consigue 17 veces más interacciones
que la imagen. El formato premia una idea partida en pasos. Castiga un post de
texto cortado en trozos.

## Cuándo usarlo en vez de un post de texto

Usa un carrusel cuando la idea tiene **secuencia**: pasos, una cuenta atrás,
una progresión de antes a después, un marco con partes. Usa un post de texto
cuando la idea es una sola afirmación. Repartir una afirmación en ocho
diapositivas es la forma más común de que un carrusel fracase, y si es lo que
tiene el usuario, díselo y pásalo a `/li-post`.

## Estructura

De 8 a 12 diapositivas. Menos de 8 es un post de texto. Más de 12 y la tasa
de finalización se desploma.

```
1        PORTADA    el gancho, 6 palabras o menos, y una línea de promesa
2        LO QUE TE JUEGAS   por qué importa, en una frase
3-N      UNA IDEA POR DIAPOSITIVA. Un titular de 3 a 7 palabras y como mucho
                    25 palabras debajo. Si necesita un párrafo, son dos.
N+1      RESUMEN    todo junto en una lista, para que la captura sirva
ÚLTIMA   LLAMADA    una acción. Seguir, comentar una palabra o el enlace. Una.
```

## Reglas para el texto

- **La portada es el 80 % del resultado.** Seis palabras. Grandes. El resto
  no salva una portada que nadie desliza. En español cuesta más: busca verbos
  cortos y quita artículos donde se pueda.
- **Numera cada diapositiva** (3/10). La finalización sube cuando se ve el
  final.
- **Ninguna diapositiva es un párrafo.** Si no cabe en 25 palabras, pártela.
- **El resumen es la que se captura.** Que se entienda sola.
- **El usuario de LinkedIn en todas**, pequeño, en una esquina de abajo. Las
  capturas viajan sin ti.
- **Titulares en minúscula salvo la primera palabra.** "Cómo cobrar por
  adelantado", no "Cómo Cobrar Por Adelantado": eso es inglés.
- **Cifras en formato español**: 4.200 €, 4,5 %, 12 de marzo.

## Cómo hacer el PDF

LinkedIn pide un PDF, a 1080x1350 (4:5) para ocupar el máximo del feed, de
menos de 100 MB y menos de 300 páginas. Hazlo en HTML e imprímelo a PDF:

```bash
# una página por diapositiva, 1080x1350, sin márgenes
# luego: Chrome sin interfaz con --print-to-pdf, o la herramienta de HTML a PDF que ya uses
```

Escribe el HTML con un `<section>` por diapositiva, `width:1080px;
height:1350px; page-break-after:always`, un solo color de acento y texto de 28
px como mínimo: se leen en el móvil, en miniatura. Declara `lang="es"` y usa
una fuente con tildes y eñes. Si el usuario tiene una skill de marca o un
sistema de diseño en este proyecto, úsalo y no te inventes una paleta.

## Salida

Primero el texto diapositiva a diapositiva, como una lista numerada que el
usuario pueda leer en diez segundos. Después el **texto del post** que la
acompaña: un carrusel necesita 2-3 líneas encima, que son el gancho real en el
feed. Pasa las dos cosas por `/li-human`. Y solo cuando el usuario apruebe el
texto, monta el PDF.

No se sube nada a LinkedIn. El PDF lo publica el usuario.

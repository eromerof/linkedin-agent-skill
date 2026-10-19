---
name: li-repurpose
description: >-
  Convierte un contenido largo (un vídeo de YouTube, un pódcast, una
  newsletter, un artículo, una transcripción o una llamada con un cliente) en
  una semana de posts de LinkedIn en español. Úsala cuando el usuario diga
  "reaprovecha esto", "sácame posts de aquí", "tengo un vídeo, una newsletter
  o una transcripción", o pegue un contenido largo y lo quiera en LinkedIn.
---

# li-repurpose

Un buen contenido largo tiene dentro de cuatro a seis posts. Casi todo el mundo
saca uno y tira el resto.

## Entrada

Una transcripción, un artículo, una newsletter, un guion, el resumen de una
llamada. Si el usuario da una URL de YouTube y hay una herramienta de
transcripción en la sesión, úsala; si no, pídele que pegue el texto. Léelo
entero antes de extraer nada.

Si el original está en inglés, no lo traduzcas: extrae las ideas y escribe los
posts directamente en español, con ejemplos, cifras y referencias que tengan
sentido para el público del usuario (euros, empresas y contexto de España si
`voice.md` no dice otra cosa). Una traducción se nota en la primera línea.

## Extrae, no resumas

El resumen de un vídeo no es un post. Nadie quiere el resumen. Repasa el
contenido y saca lo que se sostiene solo:

| qué sacar | qué es |
| --- | --- |
| **Afirmaciones** | cada frase que empezaría una discusión |
| **Cifras** | cada número, coste, duración, porcentaje |
| **Historias** | cada momento con una persona, una escena y un coste |
| **Mecanismos** | cada "esto funciona así..." |
| **Errores** | cada vez que se admite que algo salió mal |
| **Frases** | cada frase que ya se puede citar tal cual |

Haz la lista de lo encontrado, con totales, antes de escribir nada. Si salen
menos de cuatro elementos, el contenido es flojo, y cuatro posts estrujados de
ahí también lo serán. Dilo.

## Después, monta la semana

Cada elemento se convierte en un post, y cada post tiene que sostenerse solo:
el lector no ha visto el vídeo y no lo verá. Nunca escribas "como comentaba en
mi último vídeo". El post es la cosa.

Asigna a cada uno una fórmula de gancho de `li-post/hooks.json`, y varíalas:
cinco posts de la misma fuente con el mismo gancho suenan a fábrica de
contenido.

Ordénalos en la semana para que la afirmación más fuerte vaya primero, la
historia a mitad de semana y el mecanismo al final, cuando quien vio los
anteriores ya lo está esperando.

## Salida

```
FUENTE: "Por qué quitamos las llamadas de descubrimiento" (18 min, 3.400 palabras)

ENCONTRADO  4 afirmaciones, 6 cifras, 2 historias, 3 mecanismos, 1 error, 5 frases citables

SEMANA
MAR  #1  A contracorriente   Las llamadas de descubrimiento son el impuesto de tener una web mala
MIÉ  #17 El ancla de tiempo  Recuperamos 6 horas a la semana quitando un enlace de agenda
JUE  #9  Arranque en frío    "¿Hacemos una llamada rápida?"
VIE  #21 El regalo directo   El formulario de 4 preguntas que sustituyó a la llamada. Cógelo.

Di "escribe el martes" y te lo redacto.
```

Después redacta bajo petición, de uno en uno, cada uno pasando por `/li-post`
y `/li-human`. No sueltes cuatro posts terminados de golpe: sonarán todos igual
y el usuario no editará ninguno.

---
name: li-human
description: >-
  Quita la huella de máquina de cualquier borrador en español (rayas, muletillas
  de IA como "sumergirse en", "poner en valor" o "juega un papel crucial",
  caracteres invisibles) y lo puntúa con un panel de cinco pruebas antes de que
  salga. Úsala siempre que un texto tenga que sonar humano, cuando el usuario
  diga "humaniza esto", "¿esto suena a IA?", "quita las rayas", "límpialo",
  "¿me lo van a pillar?", y antes de enseñar al usuario cualquier post,
  comentario, respuesta o mensaje de LinkedIn.
---

# li-human

En esta carpeta hay dos herramientas y las dos funcionan de verdad. Úsalas. No
lo hagas a ojo.

```bash
python3 humanize.py borrador.txt --report        # limpiarlo y ver qué cambió
python3 detect.py borrador.txt                    # puntuarlo, cinco pruebas
python3 detect.py antes.txt despues.txt           # demostrar la diferencia
```

Las dos leen `slop.json`, que es el léxico: más de 350 palabras y expresiones
de relleno típicas de la IA en español con su sustitución llana (respetando
género y número), 17 clases de caracteres invisibles, 13 sustituciones
tipográficas y 19 patrones estructurales. Está hecho para editarlo. Si el
usuario usa a menudo una palabra que el léxico quita, bórrala del archivo.

## Lo que se arregla solo

**1. Caracteres invisibles.** Espacios de anchura cero, unidores, guiones
blandos, marcas de orden de bytes, caracteres de etiqueta Unicode, espacios
duros y finos. Un teclado no los produce. Sobreviven al copiar y pegar, son
invisibles en cualquier editor y son lo más mecánico de un texto generado.
`humanize.py` los borra todos, incluido cualquier carácter de formato Unicode
que no tenga nombrado.

**2. Tipografía.** Raya (—) a coma, semirraya a guion, comillas curvas y
angulares («») a rectas, elipsis a tres puntos, viñeta a guion. Ojo con la
raya: en español es correcta (RAE) para incisos y diálogos, pero en LinkedIn
casi nadie la teclea, y la raya espaciada al estilo inglés (` — `) es una de
las señales más claras de texto generado. Por eso se cambia por coma. Los
signos de apertura ¿ y ¡ no se tocan nunca: quitarlos suena a error, no a
persona.

**3. El léxico de relleno.** "En el panorama actual", "sumergirse en", "juega
un papel crucial", "poner en valor", "a día de hoy", "cabe destacar que",
"robusto", "sin fisuras", "un antes y un después", "ha llegado para quedarse",
calcos como "en base a", "es por eso que" o "hacer sentido"... Cada uno se
cambia por algo llano, manteniendo mayúsculas y sin tocar las URL. Si al borrar
una muletilla la frase empieza en minúscula, se corrige.

**4. Términos para revisar a mano.** Palabras como "clave", "fundamental",
"ecosistema", "innovador", "resiliencia" o "mi viaje" a veces están bien
usadas. No se sustituyen: salen en el informe con una pista, cuentan en la
puntuación y decides tú.

## Lo que NO se arregla solo

Los patrones estructurales se **señalan, no se reescriben**, porque cambiar la
forma de una frase exige criterio:

- "No es solo X, es Y", "No solo X, sino también Y"
- "Esto no va de X, va de Y", "No se trata de X, sino de Y", "No es X. Es Y."
- Tríadas: "la innovación, la colaboración y el crecimiento."
- Preguntas retóricas de una línea: "¿El resultado?", "¿La clave?"
- "Spoiler:" y "Esto es lo que aprendí"
- Emojis de cohete, fuego, bombilla, chispas, diana, dedo abajo y manos arriba
- Muros de hashtags
- Cebo de interacción: "¿Qué opinas?", "Te leo en comentarios", "Comenta
  INFO y te lo mando", "Sígueme para más"
- Calcos del inglés: coma antes de "y" en enumeraciones, meses y días en
  mayúscula ("en Marzo"), Títulos Con Todas Las Palabras En Mayúscula
- Mezclar "vosotros" con "ustedes", o el tuteo con "usted"
- Longitud de frase y de viñeta uniforme

Esa lista es tu trabajo. Reescribe a mano cada línea señalada conservando el
sentido y vuelve a pasar `detect.py`. Esta es la parte que lleva la nota de
REVISAR a APROBADO, y es la parte que un script no puede hacer.

Al reescribir, ten en cuenta también lo que ningún regex pilla bien en
español:

- **Sujeto de más.** "Yo creo que", "Nosotros pensamos que": el español ya
  lleva la persona en el verbo. Quita el pronombre salvo que contraste.
- **Gerundio de posterioridad.** "Lanzamos el producto, consiguiendo 200
  ventas" -> "Lanzamos el producto y conseguimos 200 ventas".
- **"Se" impersonal en cadena.** "Se analizó, se concluyó, se decidió" ->
  primera persona.
- **Registro neutro sin sitio.** Si el usuario es de España, que se note:
  "currar", "un montón", "vale", "ojo". Mira `voice.md`.

## Las cinco pruebas

`detect.py` puntúa cinco señales de 0 a 100; más alto es más humano:

| prueba | qué mide | cómo se ve la máquina |
| --- | --- | --- |
| RITMO | variación en la longitud de las frases | todas las frases igual de largas |
| CONCRECIÓN | cifras, nombres, meses, días por cada 100 palabras | sustantivos abstractos, ni un dato |
| RELLENO | términos del léxico por cada 100 palabras | vocabulario de plantilla |
| HUELLA | invisibles, rayas, comillas curvas y angulares por cada 1.000 caracteres | tipografía de imprenta |
| VOZ | coloquialismos, 1.ª y 2.ª persona, adverbios en -mente, patrones | registro de informe, giros escenificados |

El español no tiene contracciones como el inglés, así que la prueba de VOZ
busca lo que sí marca a una persona hablando: "pues", "vale", "ojo", "la
verdad", "o sea", "un montón"; "me", "mi", "te", "os"; y penaliza la cadena de
adverbios en -mente.

El veredicto pondera la media al 60 % y la **prueba más débil** al 40 %, porque
a un detector le basta una señal. APROBADO exige 70 o más de media sin ninguna
prueba por debajo de 55.

## Dilo con honestidad

Son cinco heurísticas locales basadas en las señales en las que se fijan los
detectores públicos. Se ejecutan enteras en la máquina del usuario y no se sube
nada. **No** son GPTZero, Originality, Copyleaks, Winston ni Turnitin, no
llaman a esas APIs y no pueden prometer su veredicto. Arreglar lo que miden
suele mover también esos números, porque miden lo mismo de fondo. Esa es la
afirmación. No hagas una más grande en nombre del usuario y no le digas nunca
que su texto es indetectable.

## Orden de trabajo

1. `humanize.py borrador.txt -o limpio.txt --report`
2. Lee los términos para revisar y los patrones estructurales. Reescribe esas
   líneas tú.
3. `detect.py borrador.txt limpio.txt` para enseñar el antes y el después.
4. Si el veredicto no es APROBADO, arregla la prueba más débil que indica la
   salida y repite. Dos rondas es lo normal. Cinco significa que el borrador
   se escribió con plantilla, y la solución es otro borrador, no más pasadas.
5. Enseña al usuario el texto limpio y la nota. Nunca solo la nota.

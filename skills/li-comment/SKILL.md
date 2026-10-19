---
name: li-comment
description: >-
  Escribe comentarios en español para posts de LinkedIn de otras personas que
  suenen a alguien con criterio, no a un bot. Úsala cuando el usuario pegue un
  post y quiera un comentario, diga "coméntame esto", "¿qué pongo aquí?",
  "quiero interactuar con este post", o quiera una tanda de comentarios para su
  ronda de interacción.
---

# li-comment

Comentar es lo que más rinde en LinkedIn y lo más fácil de hacer mal. Un
comentario en un post con 400 reacciones lo ve más gente que la mayoría de tus
propios posts. Uno genérico no lo ve nadie y te resta credibilidad ante el
autor.

## Entrada

El usuario pega el texto del post (y el nombre y cargo del autor si los
tiene). Si pega una captura, léela. Si te da una URL que no puedes abrir, pídele
que pegue el texto. No adivines lo que decía el post y no uses automatización
del navegador para leer el feed.

## Los nueve tipos de comentario

Elige según lo que sea el post de verdad. Nunca tires del tipo 1 por defecto.

| # | tipo | cuándo | forma |
| --- | --- | --- | --- |
| 1 | **Aportar un dato** | el post hace una afirmación que puedes respaldar con una cifra | "A nosotros nos pasó igual: el 40 % de..." |
| 2 | **El caso que falta** | el post tiene razón pero se queda corto | "Esto vale hasta que {condición}. A partir de ahí..." |
| 3 | **Discrepar con respeto** | crees de verdad que se equivoca | primero en qué estás de acuerdo, luego dónde te separas |
| 4 | **Estirar una frase** | hay una frase del post que es la buena | cítala y construye sobre ella |
| 5 | **La pregunta de verdad** | el post se ha saltado la parte difícil | una pregunta, concreta, sin "me encantaría saber" |
| 6 | **El recibo** | tú has hecho lo que describen | qué pasó, en dos frases |
| 7 | **La corrección** | hay un error de hecho | ten razón, sé breve, sé amable, asegúrate |
| 8 | **Otra lectura** | los datos están bien y el enfoque no | "Otra forma de verlo:" |
| 9 | **La frase corta** | el post no necesita nada y quieres estar | menos de 12 palabras, y que tenga gracia o sea verdad |

## Reglas

- **De 2 a 4 frases.** Más largo parece un secuestro del post. Más corto,
  relleno.
- **Nunca empieces con** "Gran post", "Me encanta", "Totalmente de acuerdo",
  "No podría estar más de acuerdo", "Muy interesante", "Interesante reflexión",
  "Qué gran aporte", "Brutal", "Gracias por compartir" ni con el nombre del
  autor seguido de exclamación ("¡Laura!"). Todos son invisibles.
- **Nada de emojis al principio.** Ni 🔥 ni 👏 ni 🙌 como primer carácter.
- **No resumas el post.** El autor sabe lo que ha escrito, y quien lo lee
  también.
- **Una idea.** Un comentario con dos ideas parece un intento de blog.
- **Di lo concreto.** Si el comentario podría ir debajo de cualquier post
  sobre el tema, no es un comentario, es ruido.
- **Discrepar está permitido y funciona**, pero el acuerdo va primero y tiene
  que ser real.
- **Mismo registro que el post.** Si el autor tutea, tutea. Si escribe desde
  Latinoamérica, no le metas "vosotros".

## Salida

Da **dos opciones de tipos distintos**, etiquetadas, y una línea con el motivo
de la que publicarías. Pasa las dos por `/li-human` antes: un comentario con
una raya se nota más que un post, porque los comentarios son cortos y la gente
los lee de cerca.

```
OPCIONES DE COMENTARIO  (en el post de @autora sobre contratación)

[6 · El recibo]
Probamos lo de contratar sin CV en 3 incorporaciones el año pasado. Dos fueron
las mejores que hemos hecho. La tercera fue un desastre, y la diferencia no
estuvo en la entrevista sino en si ya habían hecho ese trabajo antes.

[3 · Discrepar con respeto]
De acuerdo en que el CV dice poco. Pero lo que nos funcionó no fue quitarlo,
fue darle a todo el mundo la misma prueba de 90 minutos, pagada. Mismo
resultado y muchas menos discusiones internas.

Publica la primera. Son datos tuyos y reconoces un fallo, que es justo a lo
que la gente responde.
```

## Modo tanda

Si el usuario quiere una ronda de interacción, pide los 5-10 posts pegados en
un solo mensaje, devuelve un comentario por post en un único bloque y lleva
nota de a quién ha comentado ya esta semana en `~/.claude/linkedin/log.md`.
Comentar a las mismas tres personas todos los días se nota, y parece lo que es.

## Nunca

No publiques nada. No uses un navegador para publicar comentarios en nombre del
usuario. Publicar de forma automática y hacer scraping incumplen las
Condiciones de uso de LinkedIn y ponen la cuenta en riesgo. Esta skill escribe
el comentario. El usuario lo publica.

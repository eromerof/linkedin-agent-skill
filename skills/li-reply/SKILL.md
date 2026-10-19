---
name: li-reply
description: >-
  Gestiona las respuestas bajo los posts de LinkedIn del propio usuario:
  redacta en español una respuesta para cada comentario, ordenados por cuáles
  merece la pena contestar. Úsala cuando el usuario pegue los comentarios de su
  post, diga "contesta a estos", "ayúdame con los comentarios", "me han dicho X
  en mi post", o esté lidiando con un crítico o un posible cliente en los
  comentarios.
---

# li-reply

El hilo de respuestas bajo tu propio post es donde de verdad se decide el
alcance. Cada respuesta es una nueva interacción en el post, y la primera hora
de respuestas hace casi todo el trabajo. Pero no todos los comentarios valen
lo mismo, así que esta skill clasifica antes de escribir.

## Entrada

El usuario pega los comentarios, a ser posible con nombre y cargo. Las capturas
valen. No leas el hilo con un navegador.

## Primero, clasificar

Mete cada comentario en uno de estos cinco grupos y di los totales:

| grupo | qué es | qué recibe |
| --- | --- | --- |
| **CLIENTE** | alguien describiendo el problema que tú resuelves | una respuesta de verdad + una puerta abierta, suave |
| **FONDO** | aporta datos, discrepa, amplía | la respuesta más larga del hilo |
| **COLEGA** | un nombre junto al que conviene que te vean | una respuesta que le dé algo |
| **APOYO** | "gran post", 🔥, una mención | un "me gusta" y, como mucho, 3-8 palabras |
| **RUIDO** | venta, spam, mala fe | nada, o una línea y fuera |

Después escribe en ese orden y para cuando deje de merecer la pena.

## Cómo responder

- **Responde a lo que preguntan.** Si alguien pregunta cómo, dile cómo, en la
  respuesta. No le mandes a un privado para darle lo que podía tener ahí.
- **Usa su nombre una vez**, al principio, y nunca con exclamación.
- **Iguala su longitud.** Un comentario de dos líneas no recibe una respuesta
  de seis.
- **Mismo registro.** Si te tutea, tutéale. Si te escribe de usted alguien de
  un sector muy formal, responde de usted. No mezcles.
- **A un crítico:** reconoce primero lo que tiene de verdad, con sus palabras,
  y luego mantén lo que crees. Nunca borres, nunca te pongas a la defensiva,
  nunca respondas dos veces en el mismo hilo.
- **A un posible cliente:** responde completo y en público. La puerta abierta
  es una frase al final, y es una oferta de ayuda, no una venta. El valor en
  público es lo que hace que el siguiente te escriba por privado.
- **A una venta en tus comentarios:** ignórala. Contestar le da alcance.

## Salida

Un bloque, agrupado por tipo, cada respuesta lista para copiar y ya
humanizada:

```
RESPUESTAS  ·  17 comentarios  ·  1 CLIENTE, 3 FONDO, 4 COLEGA, 8 APOYO, 1 RUIDO

CLIENTE
@Marta Ruiz - "nos pasa lo mismo con los presupuestos"
> Marta, lo que nos lo arregló fue sacar la tabla de precios del documento y
> mandarla aparte. Nos quitó una ronda entera de revisiones. Si te sirve, te
> paso la plantilla.

FONDO
@Javier Ortega - no está de acuerdo con la frecuencia
> Javier, es justo. Lo de 4 días por semana funcionó porque llevaba 8 meses de
> posts detrás. Empezando de cero haría lo que dices.

APOYO  (dales "me gusta", responde a los tres primeros)
@... "Muy bueno" -> Gracias, Dani.
...

RUIDO  (1)
Ignorado: una agencia vendiendo. Contestar le da alcance.
```

Y luego la puerta: **no se publica nada hasta que el usuario diga que sí.** Las
respuestas las pega él.

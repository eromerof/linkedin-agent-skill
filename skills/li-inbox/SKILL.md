---
name: li-inbox
description: >-
  Ordena la bandeja de entrada de LinkedIn: clasifica invitaciones y mensajes
  en clientes, reclutadores, colegas, peticiones y spam, y redacta en español
  las respuestas que merece la pena mandar. Úsala cuando el usuario diga
  "tengo la bandeja hecha un desastre", "ordena mis mensajes", "¿contesto a
  esto?", pegue una tanda de mensajes de LinkedIn o esté ahogado en
  invitaciones.
---

# li-inbox

La mayoría de bandejas de LinkedIn son un 80 % ruido, y el precio de ese ruido
es que el 20 % que importa se queda una semana sin respuesta. Esta skill los
separa y luego escribe solo lo que merece la pena.

## Entrada

El usuario pega los mensajes. Las capturas valen. No entres en su cuenta ni
leas la bandeja con un navegador.

## Clasifica en cinco

| grupo | señal | acción |
| --- | --- | --- |
| **CLIENTE** | describe un problema que el usuario resuelve, o pregunta por trabajar juntos | contestar hoy, respuesta completa |
| **RECLUTADOR** | un puesto, una empresa, una banda salarial | contestar si el puesto es real; una línea si no |
| **COLEGA** | alguien del mismo sector con algo que decir | contestar esta semana, en tono humano |
| **PETICIÓN** | quiere consejo, tiempo, una presentación, un favor | contestar si es poco y concreto; declinar limpio si no |
| **SPAM** | agencia vendiendo, secuencia de captación, cripto, "una pregunta rápida" sin pregunta | archivar, sin respuesta |

Da primero los totales. Ver "3 clientes, 2 reclutadores, 41 spam" ya es la
mitad del valor.

## Detectar una secuencia

La prospección automática tiene una forma: nota de invitación sin nada
concreto, un mensaje que llega a los pocos minutos de aceptar, "una pregunta
rápida", "he visto que trabajas en {sector}", "me encantaría explorar
sinergias", un enlace a la agenda en el primer mensaje, y un "¿pudiste ver mi
mensaje?" justo cuatro días después. Delata mucho también un "Hola {Nombre}"
con el nombre completo y en mayúsculas, o un "usted" y un "tú" mezclados.
Cuando lo veas, márcalo como SPAM y di qué detalle lo delató. El usuario no le
debe una respuesta a un script.

## Respuestas

- **CLIENTE**: responde a lo que pregunta en el mensaje, entero, gratis. Si
  encaja, la oferta es una frase al final. Si no encaja, dilo y mándale a algún
  sitio útil. Las dos salidas son buenas.
- **RECLUTADOR**: si el puesto interesa de verdad, pregunta las tres cosas que
  el mensaje no dice: banda salarial bruta anual, nivel, y si es presencial,
  híbrido o en remoto. Si no interesa, una línea: no estoy buscando, encantado
  de recomendar a alguien, y que la recomendación vaya en serio.
- **PETICIÓN**: si cuesta menos de diez minutos y es concreta, hazla. Si es
  "¿te puedo robar un café para que me cuentes?", declina con una frase amable
  y dale la respuesta que le habrías dado en el café. Es la versión educada y
  también la más útil.
- **LOS NOES** son cortos, amables y definitivos. Nada de "lo retomamos después
  del verano" si no hay después del verano.

## Salida

Agrupado por tipo, totales primero, borradores solo para los grupos que llevan
respuesta, cada uno humanizado. Y la puerta: los manda el usuario.

```
BANDEJA  ·  52 mensajes  ·  3 CLIENTE, 2 RECLUTADOR, 4 COLEGA, 2 PETICIÓN, 41 SPAM

SPAM  (41) - archivar. 38 son la misma secuencia: invitación sin nada concreto,
"una pregunta rápida" a los 4 minutos de aceptar, enlace a la agenda en el
primer mensaje.
```

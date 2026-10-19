---
name: li-audit
description: >-
  Autopsia de lo que el usuario ya ha publicado: qué posts funcionaron de
  verdad, por qué y qué dejar de hacer. Úsala cuando el usuario pegue sus
  estadísticas de LinkedIn o sus posts anteriores y pregunte "¿qué me
  funciona?", "¿por qué no ha ido bien este post?", "léeme las analíticas",
  "audita mi contenido", o quiera saber dónde apostar más fuerte.
---

# li-audit

La única fuente honesta de lo que funciona en una cuenta es esa cuenta. Cada
regla de cada guía de LinkedIn, incluidas las de este paquete, es una
suposición previa. Los últimos 30 posts del usuario son la prueba.

## Entrada

Pide lo que tenga:

- La exportación de analíticas de contenido (en LinkedIn: Analíticas >
  Contenido > Exportar; según la versión puede aparecer como "Estadísticas").
  Un CSV o Excel. Ojo: si la interfaz está en español,
  los números pueden venir con coma decimal y punto de miles; léelos bien
  antes de calcular.
- O una captura por post con impresiones, reacciones, comentarios y
  compartidos.
- O solo los posts y sus reacciones, que basta para una primera pasada.

Lee también `~/.claude/linkedin/log.md` si existe, porque apunta qué fórmula de
gancho usó cada post.

## Qué medir de verdad

Las impresiones en bruto son el número menos útil de la página, porque dependen
sobre todo de cuánta gente sigue ya al usuario. Calcula esto, y enseña las
cuentas:

| métrica | cómo | qué te dice |
| --- | --- | --- |
| **Tasa de interacción** | (reacciones + comentarios + compartidos) / impresiones | si el post se ganó su alcance |
| **Ratio de comentarios** | comentarios / reacciones | si abrió conversación o solo recibió un asentimiento |
| **Múltiplo de alcance** | impresiones / seguidores | si llegó más allá del público que ya tenía |
| **Guardados y envíos** | si están disponibles | el mejor predictor de alcance futuro |

Ordena por tasa de interacción y múltiplo de alcance, no por impresiones. Un
post con 900 impresiones y 40 comentarios le gana al de 12.000 impresiones y
6.

Como referencia externa, el estudio de Metricool de 2026 dice que casi el 40 %
de las interacciones llegan el primer día y que los posts con pregunta reciben
un 77 % más de comentarios. Úsalo para contrastar, nunca en lugar de los datos
del usuario.

## Después, busca el patrón

Con los 5 mejores y los 5 peores lado a lado, busca qué los separa de verdad,
y atrévete a concluir algo que al usuario no le guste:

- Fórmula de gancho. ¿Qué números de `hooks.json` están entre los 5 mejores?
- Formato. Texto, documento, imagen, vídeo.
- Longitud.
- Tema.
- Clichés. ¿Los peores empiezan con "Hoy os quiero contar", "Spoiler:" o
  acaban en "¿Qué opináis?"? Pásalos por `detect.py` si hace falta.
- Día y hora: mira esto **lo último**, y solo si lo demás no dice nada. Casi
  nunca es la causa, y es donde todo el mundo quiere que esté. Recuerda
  también agosto, Semana Santa y los puentes antes de culpar a un día.
- Comentarios en la primera hora. Posts a los que el usuario respondió en la
  primera hora frente a los que no.

Formula el hallazgo como una afirmación con la prueba al lado, y di cuánta
confianza tienes. Con 30 posts se ve un patrón; con 6 no, y debes decir eso en
vez de inventarte uno.

## Salida

```
AUDITORÍA  ·  31 posts  ·  12 jun - 5 sep

5 MEJORES POR TASA DE INTERACCIÓN
  8,1 %  #3  La confesión   "18.000 € es lo que me costó no tener contrato"   1.940 imp.
  6,4 %  #20 Me fui         "Despedí a mi cliente que más pagaba"             2.210 imp.
  ...

5 PEORES
  0,4 %  #5  La lista       "7 herramientas que todo fundador necesita"      11.400 imp.
  ...

LO QUE DICEN LOS DATOS
1. Los posts en los que quedabas mal tú: media del 6,2 % frente al 1,1 % del
   resto. n=6. Es tu señal más fuerte y no está ni cerca.
2. Las listas de herramientas consiguen impresiones y nada más. Mucho alcance,
   cero comentarios, cero clientes. Tres de tus cinco peores.
3. El día de la semana no dice nada. Tu media del martes y la del viernes
   están dentro del ruido. Deja de optimizarlo.

DEJA DE HACER: listas de herramientas.
HAZ MÁS: los posts con un coste que pagaste tú, y una cifra.
```

Después pasa las conclusiones a `/li-plan` para que el plan de la semana
siguiente se base en las pruebas del usuario y no en valores por defecto.

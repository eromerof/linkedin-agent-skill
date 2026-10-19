---
name: li-plan
description: >-
  Planifica la semana en LinkedIn: qué publicar, cuándo publicarlo (en horario
  de España por defecto) y con quién interactuar. Úsala cuando el usuario diga
  "planifícame la semana", "¿qué publico?", "calendario de contenidos", "no sé
  de qué escribir", o quiera un calendario de publicación y una lista de
  personas con las que interactuar.
---

# li-plan

La sala de control. El resto del paquete ejecuta; esta decide qué se ejecuta.
Úsala una vez por semana, siempre el mismo día.

## Entrada

Si existen `~/.claude/linkedin/voice.md` y `log.md`, léelos: el plan no debe
repetir un tema de las dos últimas semanas. Si no existen, pide cuatro cosas y
apúntalas:

1. Qué vende el usuario y a quién.
2. Los tres o cuatro temas por los que quiere que le conozcan.
3. Qué ha pasado de verdad esta semana: una llamada con un cliente, una cifra,
   un error, algo que ha construido, una discusión. De ahí salen los posts.
4. Entre diez y veinte personas o empresas ante las que le interesa dejarse
   ver.

## Qué publicar

Cuatro posts por semana ganan a siete. La constancia es un suelo, no un
objetivo, y el quinto post de la semana casi siempre es el flojo que baja la
media.

Reparte a lo largo de la semana, nunca dos del mismo tipo seguidos:

| tipo | cuántos | para qué |
| --- | --- | --- |
| **Prueba** | 1 por semana | algo que pasó, con una cifra |
| **Opinión** | 1 por semana | una postura que podría costarte seguidores |
| **Enseñar** | 1 por semana | una cosa que el lector puede hacer hoy |
| **Historia** | 1 cada dos semanas | una escena con diálogo y un coste |
| **Oferta** | 1 cada dos semanas | lo que vendes, dicho claro, sin pedir perdón |

Para cada hueco da: el tema, el ángulo concreto sacado de lo que pasó esta
semana y el número de la fórmula de gancho de `li-post/hooks.json` que encaja.
No un tema: un ángulo. "IA" no es un plan. "El presupuesto que perdimos porque
el borrador de la IA tenía una raya en cada párrafo" es un post.

## Cuándo publicar

Publica cuando tu público está en la mesa de trabajo. Para un público B2B en
España, la referencia es **de martes a jueves, de 9:00 a 12:00**, con el pico
el jueves sobre las 11:00 y el miércoles y el viernes por la mañana justo
detrás (Metricool, estudio de LinkedIn 2026). Con el horario español, después
de las 14:00 se come y la actividad cae; el viernes por la tarde y el fin de
semana son para historias personales o para nada.

Calendario español: en agosto, en Semana Santa y en los puentes la actividad
baja mucho. Planifica menos posts esas semanas y guárdate los fuertes para
septiembre y la vuelta de vacaciones.

Si el público está en Latinoamérica, usa la misma franja de media mañana en su
hora local (según la época del año, Ciudad de México va 7-8 horas por detrás
de Madrid; Bogotá, 6-7; Buenos Aires, 4-5) y avisa de que es una referencia sin datos propios del país. Ancla siempre
la hora a la zona horaria del público, no a la del usuario, si son distintas.

Pero dilo claro: **el día y la hora importan mucho menos que una buena primera
línea.** Si el usuario está optimizando horarios antes de que le funcionen los
ganchos, está puliendo lo que no es, y tienes que decírselo.

## Con quién interactuar

Haz una lista de 10, repartida en tres:

- **5 de alcance**: gente con el público que el usuario quiere, en cuyos posts
  puede aportar de verdad. Comenta antes de que tengan 20 comentarios o no te
  verá nadie.
- **3 colegas**: mismo nivel, mismo sector. Es el grupo que devuelve la
  interacción.
- **2 compradores**: gente que podría comprar de verdad. Comenta en sus posts
  durante semanas antes de cualquier mensaje privado, y nunca vendas en un
  comentario.

20 minutos al día, antes de publicar, no después. Los comentarios en posts de
otros son lo que hace que el post propio funcione.

## Salida

```
SEMANA DEL 8 DE SEPTIEMBRE

LUN  solo interactuar  (20 min, lista abajo)
MAR  9:30   PRUEBA     #17 El ancla de tiempo  - de 5 h a 20 min en cada presupuesto
MIÉ  solo interactuar
JUE  11:00  OPINIÓN    #1  A contracorriente   - por qué quitamos la llamada de descubrimiento
VIE  10:00  ENSEÑAR    #21 El regalo directo   - el correo de 4 líneas para reabrir ventas, entero
SÁB  -
DOM  18:00  HISTORIA   #9  Arranque en frío    - el correo de "nos vamos con alguien más barato"

INTERACTUAR  (5 alcance / 3 colegas / 2 compradores)
  ...

Di "escribe el martes" y te lo redacto.
```

Escribe el plan en `~/.claude/linkedin/plan.md` para que lo lean las demás
skills. No se programa ni se publica nada en ningún sitio: esto es un plan, y
lo ejecuta el usuario.

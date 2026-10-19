---
name: li-profile
description: >-
  Puntúa un perfil de LinkedIn sobre 100 con una rúbrica de 12 apartados y
  reescribe en español lo que pierde puntos: titular, extracto (Acerca de),
  experiencia, destacados y banner. Úsala cuando el usuario diga "optimiza mi
  perfil", "puntúa mi LinkedIn", "reescríbeme el titular", "arregla mi
  extracto", o pegue su perfil y pregunte qué tal se lee.
---

# li-profile

Un perfil no es un CV. Un CV responde a "¿qué has hecho?". Un perfil responde a
"¿debería escribirle a esta persona?", y lo responde en unos cuatro segundos,
con el titular y las dos primeras líneas del extracto.

## Entrada

Pide al usuario que pegue: titular, extracto ("Acerca de"), puesto actual y las
dos últimas experiencias, y si tiene banner y sección de destacados. Para la
primera pasada basta con una captura de la cabecera. No entres en LinkedIn en
su nombre.

## Puntúalo

Lee `rubric.json` en esta carpeta. Doce apartados, 100 puntos, cada uno con lo
que significa la nota máxima. Puntúa todos, enseña la tabla y da el total. Sé
honesto: la mayoría de perfiles sacan entre 30 y 49 la primera vez, y una nota
generosa no sirve de nada.

```
NOTA DEL PERFIL  41/100

  titular              3/12   solo el cargo, sin resultado ni público
  extracto, inicio     2/10   empieza por "Apasionado por"
  extracto, cuerpo     4/10   trayectoria, no oferta
  destacados           0/8    vacío
  banner               0/6    el azul por defecto
  ...
```

## Después, reescribe en este orden

Arregla de más a menos puntos perdidos. No lo reescribas todo de golpe: el
usuario tiene que pegar cada parte él mismo.

**1. Titular (220 caracteres).** La fórmula que funciona:
`{qué haces y para quién} | {prueba} | {cómo empezar}`. No es tu cargo. Y no
empieces por "Ayudo a X a Y", que es como arranca ya un perfil de cada dos.
Evita también "Apasionado/a de", "Experto/a en" sin prueba, y las barras con
cinco cargos ("CEO | Speaker | Mentor | Inversor | Padre"). Da tres opciones.

**2. Extracto, primeras dos líneas.** Todo lo que va después de la segunda
línea queda detrás del "...ver más" en el móvil, así que esas dos líneas son el
extracto entero para la mayoría. Tienen que decir a quién ayudas y qué cambia.
Sin "apasionado", sin "orientado a resultados", sin "proactivo", sin biografía
en tercera persona y sin empezar por tu nombre.

**3. Extracto, cuerpo.** Escrito a un solo lector, tuteando (salvo que
`voice.md` diga otra cosa). Estructura: el problema que tiene, lo que haces tú,
una prueba con una cifra en formato español (1.200 clientes, un 35 %, 4.200 €),
y qué hacer a continuación. Menos de 1.400 caracteres aunque el límite sea
2.600.

**4. Destacados.** Tres elementos: tu mejor post, la prueba y la forma de
contactar. Una sección vacía son ocho puntos, y es el único sitio del perfil
que controlas del todo.

**5. Experiencia.** Cada puesto lleva una línea de alcance y de dos a tres
viñetas que son resultados con cifras, no funciones. Todo lo de hace más de
diez años, a una sola línea.

**6. Banner.** Una frase de posicionamiento y una forma de contactarte. El
degradado azul por defecto es la señal más clara de la página de que no hay
nadie en casa.

## Salida

La tabla de puntuación y después las reescrituras como bloques listos para
copiar, en orden de prioridad, cada uno ya pasado por `/li-human`. Vuelve a
puntuar al final y enseña la diferencia con honestidad: si la reescritura llega
a 88 y no a 98, di 88, y di qué necesitan los puntos que faltan (normalmente
recomendaciones, un banner de verdad y un historial de publicaciones, nada de
lo cual se arregla reescribiendo).

Esta skill no guarda nada en LinkedIn. El usuario pega cada sección.

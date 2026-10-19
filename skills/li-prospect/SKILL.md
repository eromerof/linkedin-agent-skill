---
name: li-prospect
description: >-
  Busca en LinkedIn, con Claude en Chrome y la sesión del propio usuario,
  posibles clientes y posts recientes en los que merece la pena comentar, a
  ritmo humano y con límites, y devuelve una lista corta y razonada. Úsala
  cuando el usuario diga "búscame clientes", "prospección", "busca posts para
  comentar", "¿con quién interactúo hoy?", "busca en LinkedIn gente que...", o
  quiera llenar la lista de interacción de /li-plan. Nunca publica, comenta,
  conecta ni envía mensajes por su cuenta.
---

# li-prospect

Encuentra a las 10-15 personas o posts de esta semana que merecen tus 20
minutos de interacción, y te dice por qué. No monta bases de datos ni escribe
nada en LinkedIn. Lee, filtra y propone. Lo que se publica lo publica el
usuario.

## Antes de empezar

1. Lee `cliente-ideal.md` en esta carpeta: a quién se busca, qué señales
   importan, qué palabras clave usar y a quién descartar. Si tiene marcas
   `[?]` que afectan a la búsqueda de hoy, pregunta una vez y sigue.
2. Lee `~/.claude/linkedin/voice.md`, `plan.md` y `prospectos.md` si existen:
   no repitas a nadie de las últimas cuatro semanas ni un tema que ya cubre el
   plan.
3. Comprueba que tienes las herramientas de Claude en Chrome (navegar, leer la
   página, buscar en la página, capturas). Si no las tienes, dilo y pasa al
   **modo manual**: el usuario hace la búsqueda y pega aquí los resultados, y
   tú haces el filtrado y la lista igual.
4. Pregunta, en una sola pregunta agrupada y solo si no está claro: ¿posts para
   comentar, personas para conectar, o las dos cosas? ¿Algún tema o sector
   concreto esta semana?

## Límites de cada sesión

LinkedIn prohíbe en sus Condiciones de uso los bots y la extracción
automatizada, y detecta la actividad que no parece humana. Una restricción de
la cuenta le cuesta al usuario su principal canal. Estos límites no son
opcionales:

- **Una sesión al día**, como mucho.
- **3 búsquedas** por sesión, como mucho.
- **40 posts leídos** y **15 perfiles abiertos** por sesión, como mucho. Abrir
  un perfil le avisa a esa persona de que lo has visitado: abre solo los que
  ya han pasado el filtro del post.
- **Ritmo de persona**: lee cada página entera antes de pasar a la siguiente,
  sin abrir pestañas en paralelo y sin desplazarte sin parar por resultados.
- **Nada de Sales Navigator, exportaciones, listas masivas** ni recorrer
  páginas de seguidores o de empleados de una empresa.
- **Si LinkedIn muestra un captcha, un aviso de actividad inusual o te pide
  iniciar sesión, para en el acto** y díselo al usuario. No lo intentes
  sortear.
- **No escribas nada en LinkedIn**: ni comentarios, ni reacciones, ni
  invitaciones, ni mensajes, ni "seguir". Ver *Después de la lista*.

## Cómo buscar

**Posts recientes.** Usa la búsqueda de contenido con palabras clave de
`cliente-ideal.md`, ordenada por fecha y de la última semana. Esta URL suele
funcionar; si LinkedIn la cambia, usa los filtros de la interfaz (Publicaciones
→ Fecha de publicación → Última semana → Ordenar por: Más recientes):

```
https://www.linkedin.com/search/results/content/?keywords=<palabras>&datePosted=%22past-week%22&sortBy=%22date_posted%22
```

**Personas.** Búsqueda de personas por cargo y palabras clave, filtrada a
España (Ubicación → España). Úsala menos que la de posts: un post cuenta qué le
pasa a alguien; un perfil solo dice quién es.

**Tu propio feed.** Si el usuario lo pide, lee las primeras pantallas de su
feed: ahí están los posts de su red, donde un comentario rinde más.

Para cada resultado, lee el post entero (pulsa "...más" si hace falta) y la
línea de cargo del autor. Abre el perfil solo si el post encaja y necesitas
confirmar empresa, tamaño o ubicación.

## Cómo filtrar

Puntúa cada candidato con estas cuatro preguntas, de 0 a 2 cada una:

| pregunta | 0 | 1 | 2 |
| --- | --- | --- | --- |
| **¿Encaja el perfil?** | no es cliente (ver lista de descartes) | encaja a medias | cargo y empresa encajan |
| **¿Hay señal de problema?** | ninguna | indirecta (crecimiento, contrataciones) | cuenta el problema que el usuario resuelve |
| **¿Es reciente?** | más de 2 semanas | de 3 a 14 días | últimas 72 horas |
| **¿Se puede aportar algo?** | solo cabría "gran post" | un comentario correcto | un dato, un caso o una pregunta que nadie ha hecho |

Quédate con los de 5 o más. Descarta sin dudar a la competencia, a
reclutadores y a quien solo vende su producto, aunque el post sea bueno.

Nunca inventes datos de una persona. Si no sabes el tamaño de la empresa,
pon "tamaño sin confirmar" en vez de adivinarlo.

## Qué acción propones

Para cada candidato, una sola:

- **COMENTAR**: el post encaja y aún tiene pocos comentarios (mejor si menos
  de 20). Pasa a `/li-comment`.
- **CONECTAR**: encaja muy bien y hay un motivo concreto para escribir hoy
  (este post). Mejor si antes ha recibido un comentario tuyo. Pasa a `/li-dm`.
- **SEGUIR DE CERCA**: encaja, pero ahora no hay nada que aportar. Apúntalo y
  vuelve la semana que viene.
- **NADA**: no pasa el filtro. No hace falta listarlos uno a uno, solo el
  total.

Vender en un comentario o conectar sin haber interactuado nunca son las dos
formas más rápidas de quemar a un buen candidato. Si dudas entre COMENTAR y
CONECTAR, elige COMENTAR.

## Salida

```
PROSPECCIÓN  ·  19 oct  ·  3 búsquedas, 36 posts leídos, 6 perfiles abiertos
12 candidatos  ·  7 COMENTAR, 2 CONECTAR, 3 SEGUIR DE CERCA  ·  24 descartados

COMENTAR
1. Laura Gómez · Gerente · Distribuciones Gómez (≈40 empl., Valencia)   8/8
   "Tres años intentando que el almacén y la oficina usen el mismo Excel..."
   hace 1 día · 6 comentarios · <enlace al post>
   Por qué: cuenta tu problema exacto; puedes aportar cómo se ordena antes de
   elegir herramienta.

2. ...

CONECTAR
1. Jorge Martín · Director de operaciones · Instalaciones Martín (tamaño sin confirmar, Zaragoza)   7/8
   Le comentaste el 12 oct; hoy pregunta qué ERP elegir.  <enlace al perfil>

SEGUIR DE CERCA
...

Di "comenta el 1, 2 y 4" y te los redacto con /li-comment.
```

Los enlaces van completos para que el usuario los abra con un clic.

## Después de la lista

- Redacta los comentarios con `/li-comment` y las invitaciones con `/li-dm`,
  siempre pasados por `/li-human`.
- **El usuario publica.** Le das el texto listo para copiar y el enlace, y él
  lo pega y pulsa "Publicar" o "Enviar". Solo si el usuario lo pide de forma
  explícita para un elemento concreto, puedes abrir ese post y escribir el
  texto aprobado en la caja de comentario o en la nota de invitación, **sin
  pulsar nunca "Publicar", "Enviar" ni "Conectar"**: ese clic es siempre suyo.
- En Claude Code, añade cada candidato propuesto a
  `~/.claude/linkedin/prospectos.md` (fecha, nombre, cargo, empresa, enlace,
  acción y motivo) para no repetirlo. En claude.ai, ofrece la tabla para que el
  usuario la guarde en su Proyecto.

## Datos personales

Son datos de personas reales y el usuario está en España (RGPD). Guarda solo
lo mínimo para hacer seguimiento: nombre, cargo, empresa, enlace público,
motivo y fecha. Nada de correos, teléfonos ni datos que no estén en el post o
en la cabecera del perfil. Propón borrar del registro lo que tenga más de 90
días sin ninguna interacción.

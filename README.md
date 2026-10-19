# La skill de LinkedIn para agentes, en español

Doce skills de Claude para llevar una cuenta de LinkedIn **en español**. Sin
registro, sin clave de API, nada que conectar.

No es una traducción. Es una adaptación del
[original en inglés de Jake Schincariol](https://github.com/Jakeschincariol/linkedin-agent-skill)
al público hispanohablante, con España como variante por defecto: léxico de
IA en español, clichés de LinkedIn España, tipografía de la RAE, formatos
numéricos españoles, horarios de publicación en hora peninsular y ganchos
escritos para este público.

Una skill escribe tus posts a partir de 21 fórmulas de gancho. Otra comenta en
posts ajenos. Otra gestiona las respuestas bajo los tuyos. Otra puntúa tu
perfil sobre 100 y reescribe lo que pierde puntos. Otra planifica la semana:
qué publicar, cuándo y con quién interactuar. Otra busca en LinkedIn, con
Claude en Chrome, posibles clientes y posts donde comentar.

Y una es el humanizador, que es lo que hace que el resto se pueda usar. Quita
las rayas, el vocabulario de plantilla ("sumergirse en", "poner en valor",
"juega un papel crucial") y los caracteres invisibles de un borrador, y luego
puntúa lo que queda con un panel de cinco pruebas antes de que lo veas.

**No se publica nada hasta que digas que sí.** Estas skills escriben. Tú
publicas.

## Instalación

Este repositorio es privado: necesitas acceso y tener `git` o `gh`
autenticado con tu cuenta.

En Claude Code:

```bash
git clone https://github.com/eromerof/linkedin-agent-skill.git
cp -r linkedin-agent-skill/skills/li-* ~/.claude/skills/
```

O como plugin:

```
/plugin marketplace add eromerof/linkedin-agent-skill
/plugin install linkedin-agent
```

En claude.ai o Claude Desktop (que no pueden leer un repositorio privado),
usa los zips de [`dist/`](dist/):

- **`linkedin-agent.zip`**: el plugin completo, con las 12 skills y su
  `.claude-plugin/plugin.json`. Súbelo como plugin y lo tienes todo de una vez.
- **`li-*.zip`**: una skill por zip, con el `SKILL.md` en la raíz, por si
  prefieres instalar solo algunas desde Ajustes → Capacidades → Skills.

Activa también la ejecución de código, que `li-human` necesita para sus
scripts. Si cambias alguna skill, regenera los zips desde la raíz del
repositorio:

```bash
rm -f dist/*.zip
zip -qr dist/linkedin-agent.zip .claude-plugin/plugin.json skills templates README.md LICENSE -x "*/__pycache__/*" "*.DS_Store"
cd skills && for d in li-*; do (cd $d && zip -qr ../../dist/$d.zip . -x "__pycache__/*" "*.DS_Store"); done
```

Para un solo proyecto en vez de global, copia las mismas carpetas en
`.claude/skills/` dentro del repositorio. ¿Sin Claude Code? Pega cualquier
`SKILL.md` al principio de un chat y funciona como un modo: pierdes las dos
herramientas de Python, que son casi todo el sentido de `/li-human`, pero el
resto funciona.

Después dedica diez minutos a `templates/voice.md`. Cópialo en
`~/.claude/linkedin/voice.md` y rellénalo, o pega tres posts tuyos en Claude y
di "escríbeme el voice.md a partir de estos". Ahí se fija también la variante
del español (España, México, Argentina...) y si tuteas o no. Todas las skills
leen ese archivo. Si te lo saltas, todo sale sonando como todo el mundo.

## Las doce

| comando | qué hace |
| --- | --- |
| `/li-post` | De una idea a un post. Tres ganchos de [21 fórmulas](skills/li-post/hooks.json), un borrador completo, humanizado antes de que lo veas. |
| `/li-comment` | Comentarios en posts ajenos. Nueve tipos, elegidos según lo que es el post. Nunca "¡Gran post!". |
| `/li-reply` | El hilo bajo tu propio post. Clasifica cada comentario en cliente / fondo / colega / apoyo / ruido y responde en ese orden. |
| `/li-profile` | Puntúa tu perfil con una [rúbrica de 12 apartados](skills/li-profile/rubric.json) sobre 100 y reescribe por orden de prioridad. |
| `/li-plan` | La semana. Qué publicar, cuándo (hora de España por defecto) y las 10 personas con las que interactuar. Escribe `~/.claude/linkedin/plan.md`. |
| `/li-human` | El humanizador. Dos scripts que funcionan de verdad. Más abajo. |
| `/li-carousel` | Carruseles. El texto diapositiva a diapositiva, la portada que consigue el deslizamiento y el PDF para subir. |
| `/li-repurpose` | Un vídeo, newsletter o transcripción convertido en una semana de posts que se sostienen solos. Si el original está en inglés, no lo traduce: lo reescribe para tu público. |
| `/li-dm` | La nota de invitación de 200 caracteres, el primer mensaje y los dos seguimientos. Dos. |
| `/li-inbox` | Ordena la bandeja en cliente / reclutador / colega / petición / spam, y te dice qué detalle delató la secuencia automática. |
| `/li-audit` | Autopsia de lo que ya has publicado. Ordena por tasa de interacción y múltiplo de alcance, no por impresiones. |
| `/li-prospect` | Busca con Claude en Chrome, en tu sesión y a ritmo humano, posibles clientes y posts recientes donde comentar, según tu [cliente ideal](skills/li-prospect/cliente-ideal.md). Devuelve 10-15 candidatos con el motivo y la acción. No escribe nada en LinkedIn. |

## El humanizador

`/li-human` trae dos scripts de Python sin dependencias. Se ejecutan en tu
máquina, sobre tu texto, y no se sube nada.

```bash
python3 humanize.py borrador.txt --report      # limpiarlo y ver cada cambio
python3 detect.py borrador.txt                  # puntuarlo, cinco pruebas
python3 detect.py antes.txt despues.txt         # demostrar la diferencia
```

**Lo que se quita solo:**

- **Caracteres invisibles.** Espacios de anchura cero, unidores, guiones
  blandos, marcas de orden de bytes, caracteres de etiqueta Unicode, espacios
  duros y finos. Tu teclado no los produce. Sobreviven al copiar y pegar y son
  invisibles en cualquier editor.
- **Tipografía.** Raya a coma, semirraya a guion, comillas curvas y angulares
  («») a rectas, elipsis a tres puntos. La raya es correcta en español, pero en
  LinkedIn casi nadie la teclea, y la raya espaciada al estilo inglés (` — `)
  delata al modelo. Los signos ¿ y ¡ no se tocan.
- **El léxico.** Unas 360 palabras y expresiones típicas de la IA en español,
  con su sustitución llana respetando género y número: "en el panorama
  actual", "sumergirse en", "robusto", "sin fisuras", "un antes y un después",
  "poner en valor", "a día de hoy", "cabe destacar que", y calcos del inglés
  como "en base a", "es por eso que", "hacer sentido" o "jugar un papel
  crucial". Mantiene las mayúsculas, no toca las URL y, si al borrar una
  muletilla la frase empieza en minúscula, la corrige. Vive en
  [`slop.json`](skills/li-human/slop.json) y está hecho para editarlo.

**Lo que se señala para revisar a mano:** 41 términos que a veces están bien
usados ("clave", "fundamental", "ecosistema", "innovador", "resiliencia", "mi
viaje"). Cuentan en la puntuación, pero decides tú.

**Lo que se señala en vez de arreglarse:** "No es solo X, es Y", "Esto no va
de X, va de Y", "No se trata de X, sino de Y", tríadas, preguntas retóricas de
una línea ("¿El resultado?"), "Spoiler:", muros de hashtags, cebo de
interacción ("Te leo en comentarios", "Comenta INFO y te lo mando"), coma
antes de "y", meses en mayúscula, Títulos Con Todas Las Palabras En
Mayúscula, mezclar "vosotros" con "ustedes" y longitud de frase uniforme.
Cambiar la forma de una frase exige criterio, así que eso se devuelve para
reescribir en vez de destrozarlo con una expresión regular.

**Las cinco pruebas**, de 0 a 100, más alto es más humano:

| prueba | qué mide |
| --- | --- |
| RITMO | variación en la longitud de las frases. Los modelos escriben parejo. |
| CONCRECIÓN | cifras (4.200 €, 4,5 %), nombres, meses y días por cada 100 palabras |
| RELLENO | términos del léxico por cada 100 palabras |
| HUELLA | invisibles, rayas, comillas curvas y angulares por cada 1.000 caracteres |
| VOZ | coloquialismos ("pues", "vale", "ojo"), 1.ª y 2.ª persona, adverbios en -mente, patrones |

El español no tiene contracciones como el inglés, que es lo que usaba el
original para medir la voz, así que esta versión mide lo que sí delata a una
persona escribiendo en español.

El veredicto pondera la media al 60 % y la **prueba más débil** al 40 %,
porque a un detector le basta una señal.

Con un borrador deliberadamente malo ("En el panorama actual, la inteligencia
artificial juega un papel crucial..."):

```
  RITMO         ########................  34,2
  CONCRECIÓN    ################........  66,0
  RELLENO       ........................   0,0    27 términos de relleno, 22,3 por cada 100 palabras
  HUELLA        ###################.....  79,2    1 raya espaciada
  VOZ           ##......................  10,4    8 patrones estructurales
  ------------------------------------------------------------
  NOTA HUMANA   #####...................  22,8   SOSPECHOSO
```

Después de `humanize.py`, con los patrones estructurales aún sin reescribir:

```
  NOTA HUMANA   ##########..............  42,0   SOSPECHOSO   (+19,2)
```

Un post escrito por una persona, con cifras, nombres y alguna expresión
coloquial, saca 89,9 y APROBADO. Lo que queda entre el 42 y el aprobado es,
a propósito, trabajo tuyo.

## Qué se ha adaptado al español

- **Léxico propio**, no traducido: muletillas de los modelos en español,
  calcos del inglés y postureo de LinkedIn España ("aportar valor", "Feliz de
  anunciar", "Ahí lo dejo", "Dato mata relato").
- **Tipografía de la RAE y la Fundéu**: raya, comillas angulares, ¿ y ¡,
  meses en minúscula, sin coma antes de "y".
- **Formatos españoles**: punto de miles, coma decimal, euro detrás
  (4.200 €), "un 30 %".
- **Horarios de España**: de martes a jueves, de 9:00 a 12:00, con el pico el
  jueves a las 11:00 ([Metricool, 2026](https://metricool.com/es/mejor-hora-para-publicar-en-linkedin/)),
  teniendo en cuenta la hora de comer, agosto, Semana Santa y los puentes.
- **Registro**: tuteo por defecto, también en B2B; aviso si se mezcla tú y
  usted o vosotros y ustedes.
- **Ganchos y ejemplos** escritos para este público, con euros, empresas y
  situaciones de aquí.

## La letra pequeña, que es la parte honesta

**Estas skills no publican en LinkedIn, y no deberían.** No hay una API
oficial para publicar en un perfil personal sin una app de partner aprobada, y
automatizar la web con un navegador o una herramienta de terceros incumple las
[Condiciones de uso de LinkedIn](https://www.linkedin.com/legal/user-agreement)
y acaba con cuentas restringidas. Por eso todas las skills terminan igual: un
bloque listo para copiar, y lo pegas tú. No es una limitación añadida después,
es el diseño. Y es lo que hace que la puerta de aprobación sea real y no una
opción de configuración.

**`/li-prospect` sí abre LinkedIn, y eso tiene riesgo.** Lee búsquedas y posts
con Claude en Chrome, dentro de tu propia sesión. Las Condiciones de uso de
LinkedIn prohíben los bots y la extracción automatizada, así que la skill
trabaja como lo harías tú: una sesión al día, 3 búsquedas, 40 posts y 15
perfiles como mucho, sin exportar nada y parando ante cualquier captcha o
aviso. Aun así, el riesgo no es cero, y la decisión de usarla es tuya. Lo
único que nunca hace es escribir en LinkedIn: comentar, conectar, enviar o
publicar sigue siendo un clic tuyo.

**Las cinco pruebas son heurísticas locales, no APIs de detectores.** Están
basadas en las señales en las que se fijan los detectores públicos y se
ejecutan enteras en tu máquina. No son GPTZero, Originality, Copyleaks,
Winston ni Turnitin, no llaman a esos servicios y no pueden prometer sus
veredictos. Arreglar lo que miden suele mover esos números, porque miden lo
mismo de fondo. Esa es toda la afirmación. Nadie puede venderte honestamente
algo "indetectable", y quien lo haga te está vendiendo otra cosa.

**La limpieza de caracteres invisibles es real y es acotada.** Quita los
caracteres de anchura cero y de formato que acaban en el texto generado y
sobreviven al copiar y pegar. Es una huella real y comprobable. No es una
afirmación sobre romper un sistema de marca de agua criptográfica, y este
repositorio no la hace.

**Nada de esto se inventa nada.** Ni métricas, ni clientes, ni resultados a tu
nombre. Si un borrador necesita una cifra que no has dado, vuelve con
`{{tu cifra}}` dentro y un aviso, siempre.

## Archivos

```
skills/li-post/hooks.json        21 fórmulas de gancho: plantilla, ejemplo, para qué sirve y cómo se estropea
skills/li-human/slop.json        el léxico: ~360 términos, 17 clases de invisibles, 19 patrones estructurales
skills/li-human/humanize.py      las tres pasadas de limpieza
skills/li-human/detect.py        el panel de cinco pruebas
skills/li-profile/rubric.json    la nota del perfil sobre 100
skills/li-prospect/cliente-ideal.md   a quién busca /li-prospect. Revísalo.
templates/voice.md               tu perfil de voz. Rellénalo primero.
dist/linkedin-agent.zip          el plugin completo, para subir de una vez a claude.ai o Claude Desktop
dist/li-*.zip                    una skill por zip, con el SKILL.md en la raíz
```

## Créditos

Original de Jake Schincariol, [opusjake.ai](https://opusjake.ai), con licencia
MIT: [Jakeschincariol/linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill).
Esta versión adapta el contenido, el léxico y las heurísticas al español.

## Licencia

MIT. Cógelo, cámbialo, úsalo.

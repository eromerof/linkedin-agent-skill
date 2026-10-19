Enrique Romero es un consultor independiente de Microsoft Power Platform y Dynamics 365 que trabaja con pymes españolas. Su lema es «estructura antes que tecnología». La identidad la desarrolló Agarimo Estudio (diagnóstico y plataforma de marca) y este documento la traduce en reglas de uso. La estrategia completa (propósito, valores, arquetipo) está en la sección *Estrategia de marca*; lo que aún no está decidido está en *Pendiente de definir*.

Usa los archivos así: lee este documento, aplica `tokens.json` (colores y estilos de texto), copia los logotipos de `assets/Logotipo/` sin redibujarlos y parte del componente que se parezca a la pieza que vas a hacer (`components/`: `Logo`, `Boton`, `NumeroTitulo`, `PiePost`, `PostCuadrado`, `Carrusel`, `PropuestaPPT`, `PropuestaA4`, `CabeceraWeb`, `BloqueDestacado`, `BannerLinkedin`).

## Fundamentos de contenido

La marca promueve soluciones tecnológicas «desde una perspectiva humanista, práctica y de eficiencia». Todo lo que se escriba debe sonar a una persona, no a una empresa de tecnología.

- **Tú, primera persona.** Háblale al cliente de tú y habla de ti en primera persona: «Cuenta conmigo», «Estoy aquí para escucharte», «Mis servicios se dividen en 3 grandes bloques».
- **Sin palabrejas técnicas.** Explica el problema, el resultado esperado y la rentabilidad, no la especificación. Si un término técnico es inevitable, acompáñalo de una frase llana.
- **Cálido y tranquilizador, nunca «canallita».** Transmite seguridad, confianza y resolución. No mezcles tono comercial agresivo con marca personal.
- **Transparente.** Di lo que se puede y lo que no. «Si no sé algo, lo admitiré y trabajaré para encontrar la respuesta correcta.»
- **Preguntas al cliente como gancho.** Los titulares de dolor son preguntas reales: «¿Tus procesos empresariales son lentos y poco eficientes provocando que la empresa pierda dinero?», «¿Sabes lo que es la micro-optimización?».
- **Etiquetas y botones en MAYÚSCULAS**, cortos y directos: «VER SERVICIOS», «CONTACTAR», «SÍ, CLARO», «NI IDEA», «VER CÓMO». Los enlaces secundarios llevan prefijo «+ »: «+ SOBRE MÍ», «+ VER CASOS DE ÉXITO».
- **Titulares en minúscula normal** salvo la primera letra: «Descubriendo nuevos retos», «Cómo lo hago», «Mi perspectiva».
- **Sin emojis.** Ninguna pieza de Agarimo los usa.
- **Firma.** Nombre «ENRIQUE ROMERO» con la frase «Soluciones tecnológicas personalizadas» (lockup), handle `@enriqueromero`, web `enriqueromero.es`, correo `hello@enriqueromero.es`.

Antes de publicar cualquier pieza hazte las preguntas de marca: ¿está representado nuestro tono de voz?, ¿comunicamos nuestro propósito?, ¿aportamos valor a la audiencia?, ¿nos acerca a nuestro objetivo?, ¿está presente nuestra personalidad?, y si la marca fuera una persona, ¿haría esto?

## Fundamentos visuales

**Idea general.** Minimalismo con fondo blanco, mucho aire, una sola nota de color y una regla fina negra que ordena. Es una identidad *boutique* pero cercana a la tecnología: ni lujo clásico, ni el azul corporativo del sector. Debe poder gestionarse sin diseñador y repetirse igual siempre.

**Color.**
- Fondo de página: `blanco`. Bandas y bloques de apoyo: `superficie`. Texto: `negro`.
- `violeta` es el único acento. Úsalo como «punto de luz»: un titular grande, un número editorial, un botón. Si todo es violeta, nada destaca.
- Texto violeta solo en **titulares** (5,73:1 sobre `blanco`, 5,21:1 sobre `superficie`). Nunca en cuerpo ni en texto pequeño; vibra y pierde legibilidad. Sobre `negro` el violeta (3,67:1) queda para gráficos o titulares de 24px o más.
- Sobre `negro` el texto va en `blanco`. `superficie` como texto sobre negro no se recomienda.
- `texto-secundario` (#999999) solo sobre `negro` (7,37:1). En fondos claros no cumple contraste (2,85:1 sobre blanco): usa `negro`.
- `divisor` separa elementos dentro de un bloque. Las reglas estructurales son `negro`: 2px en los posts (bajo la cabecera y sobre el pie), 1px en la propuesta A4 y bajo el menú de la web.
- Sin degradados, sin sombras decoradas, sin colores secundarios. Agarimo descartó el naranja, el amarillo y el rojo («desmarcan en exceso») y los azules típicos del sector.

**Tipografía.** Sora en toda la jerarquía: titulares, cuerpo y etiquetas. **Siempre Sora, nunca otra fuente** (ni Calibri en propuestas). Pesos: Thin 100, ExtraLight 200, Light 300, Regular 400, Medium 500, SemiBold 600, Bold 700, ExtraBold 800. Medium (500) es el peso de los títulos y cifras violeta de la propuesta A4, el subtítulo de los posts y la web; Light 300 para el cuerpo; Bold 700 para la frase que debe quedarse en carruseles y propuestas. Usa los estilos de `tokens.json` (`post-*`, `carrusel-*`, `prop-*`, `a4-*`, `banner-*`, `web-*`) en lugar de tamaños sueltos. Los tamaños de posts, A4 y banner están medidos en las maquetas de Agarimo; los de la web, en el sitio publicado.

Mayúsculas solo en etiquetas y botones, escritas ya en mayúsculas.

**Patrón editorial.** Número grande + título en violeta: `NumeroTitulo`. «01.» en `post-numero` (o `web-numero`, `a4-numero`) y debajo el título en `violeta`; el texto de apoyo en `negro`. Se numera siempre con dos cifras y punto en la web y en los posts.

**Maquetación.**
- Todo es de esquinas rectas: botones, tarjetas, posts, hojas. No hay radios definidos.
- Cabecera y pie encuadrados por una regla negra fina; el contenido respira en el centro con márgenes amplios.
- Banda lateral violeta vertical como acento (portada de post, bloque «Mis servicios…», tarjetas de pregunta en la web): es un recurso real de la marca, úsalo con moderación y solo con fondo `superficie` o `blanco`.
- Fotografía y bloques de apoyo pueden sangrar hasta el borde de la pieza.

**Formatos.**
- **Post cuadrado 1080×1080 y vertical 1080×1350** (redes): cabecera con `@enriqueromero`, contenido, pie «Recomienda / Comenta / Comparte»; márgenes de 108px y reglas negras de 2px. Componentes `PostCuadrado` y `PiePost`.
- **Banner de LinkedIn 1584×396**: `BannerLinkedin`.
- **Carrusel de LinkedIn (1080×1350px)**: posts verticales con el marco de `PiePost`, contador de página y cierre con acción. Estilos `carrusel-*`. Componente `Carrusel`.
- **Propuesta en diapositivas 16:9 (1280×720px), formato preferido**: título violeta, cifra grande + frase, fases en tarjetas, bloque de voz, datos del cliente entre corchetes. Estilos `prop-*`. Componente `PropuestaPPT`.
- **Propuesta comercial A4 (794×1123px)**, para documentos: portada con el lockup arriba, «Propuesta» en `violeta`, «Personalizada para …», pie con `enriqueromero.es` y `hello@enriqueromero.es`; páginas interiores con cabecera (nombre del cliente a la izquierda, lockup a la derecha) y regla negra; márgenes de 79px. Componente `PropuestaA4`.
- Agarimo también diseñó una tarjeta de visita vertical y una plantilla de presentación y de Word; no hay componente para ellas todavía.
- **Web** `enriqueromero.es` (diseño de Agarimo sobre Framer): cabecera con lockup y menú, héroe con título violeta y botón, tarjetas de pregunta, servicios numerados. Componentes `CabeceraWeb`, `Boton`, `NumeroTitulo`, `BloqueDestacado`.

**Logotipo.** Usa siempre los archivos de `assets/Logotipo/`; no lo redibujes, no lo recolorees, no lo estires.
- Sobre `blanco` o `superficie`: lockup negro, o negro con frase violeta.
- Sobre `violeta` o `negro`: lockup blanco.
- Formato apilado («ENRIQUE / ROMERO») cuando no cabe el horizontal.

## Iconografía

Los iconos de la marca son pocos y de línea fina: avión de papel (compartir), marcador (guardar), flecha larga hacia la derecha (botones «VER SERVICIOS →»). En la web aparecen además pines de ubicación violetas con una ruta de trazos que enlaza los tres servicios. No hay un set de iconos propio ni ficheros de iconos entregados: hasta que se defina, mantén iconos de línea fina del mismo grosor que el trazo de Sora, en `negro` o en `violeta` sobre claro, y no uses emojis. Ver propuesta en *Pendiente de definir*.

## Fotografía

Sesión de estudio real de Enrique: fondo gris liso y claro, luz suave y natural, ropa sencilla (camisa azul grisácea, camisa blanca, camiseta rosa pálido, vaqueros claros). Poses relajadas y sonrientes: sentado, con los brazos cruzados, con el portátil, charlando con otra persona y tocando la trompeta (la música es su pasión fuera del trabajo). Es una imagen cercana y humana, no un banco de imágenes genérico. Las 10 fotos elegidas están en `assets/Fotografia/`, con su descripción en el README del grupo.

- Recorta con `object-fit: cover` a la proporción de la pieza, sin deformar.
- Sin filtros de color ni tratamientos duotono: el gris neutro de fondo deja respirar el `violeta` de la pieza.
- La foto sangra hasta el borde de la pieza (post C, página 2 de la propuesta); el resto de la pieza es plano.
- Retratos de cerca para presentaciones y «Sobre mí»; fotos con portátil o con otra persona para servicios y propuestas.

Aún no hay fotografía de casos de éxito ni de clientes. Si faltan, no uses imágenes de stock: ver *Pendiente de definir*.

## Reglas de uso

1. Fondo `fondo`, texto `texto`, un solo `acento` por pieza.
2. Titulares en `violeta` o `negro`; cuerpo siempre en `negro`.
3. Solo Sora, en cualquier peso de la escala (Medium 500 incluido).
4. Etiquetas y botones en mayúsculas; títulos en minúscula normal.
5. Esquinas rectas, sin sombras, sin degradados.
6. Logotipo solo desde `assets/Logotipo/`, con la versión adecuada al fondo.
7. Todo texto cumple 4,5:1 (3:1 en 24px o más). `texto-secundario` solo sobre `negro`.
8. Si una pieza necesita algo que no está aquí (espaciado, radios, sombras, iconos, modo oscuro, zona de respeto del logotipo), no lo inventes: está en *Pendiente de definir*.

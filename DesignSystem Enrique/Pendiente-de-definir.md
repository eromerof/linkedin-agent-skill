# Pendiente de definir

Estos puntos no están decididos ni en el brief ni en los documentos de Agarimo. **Nada de lo que sigue está en `tokens.json` ni se aplica en los componentes** hasta que Enrique lo apruebe: son propuestas para consultar, cada una con lo que sí dicen las fuentes.

## 1. Escala de espaciado

**Qué dicen las fuentes:** nada explícito, pero las maquetas dan medidas: margen de 108px en los posts, bandas de cabecera y pie de 107px (cuadrado) y 128px / 126px (vertical), margen de 79px en la A4, botones de 60px de alto en la web. Los componentes usan esos valores sueltos, sin tokens de espaciado.

**Propuesta:** base de 8px: 4, 8, 16, 24, 32, 48, 64, 96, 128. Tokens `space-1` a `space-9`. Margen exterior de pieza: 108px en un post de 1080px y 79px en la A4 (lo que miden las maquetas de Agarimo).

**Para decidir:** ¿mantenemos la base de 8px y estos pasos? ¿Qué margen exterior prefieres en el post?

## 2. Radios de borde

**Qué dicen las fuentes:** todos los elementos de marca (botones, tarjetas, posts, hojas, banda violeta) son de esquinas rectas. Solo los campos de formulario que aporta la plataforma de la web tienen 8px.

**Propuesta:** un único valor, `radius-0` (esquinas rectas), para todo. Si algún día hace falta un formulario, 8px solo en campos.

**Para decidir:** ¿esquinas rectas siempre, sin excepciones?

## 3. Sombras

**Qué dicen las fuentes:** las sombras de las maquetas de Agarimo son del mockup (para presentar las piezas), no de las piezas. Las piezas son planas, separadas por reglas finas.

**Propuesta:** sin sombras. La jerarquía se consigue con `superficie`, reglas negras de 1px y espacio.

**Para decidir:** ¿sin sombras, o quieres una sola elevación sutil para menús o ventanas flotantes?

## 4. Estilo de iconografía

**Qué dicen las fuentes:** iconos de línea fina (avión de papel, marcador, flecha larga). En la web hay pines de ubicación violetas con una ruta de trazos que enlaza los servicios.

**Propuesta:** familia de iconos de línea de 1,5px de trazo, esquinas redondeadas del propio trazo, cuadrícula de 24px, en `negro` o `violeta` sobre claro. Sin rellenos, sin iconos de colores. Habría que dibujar o elegir el set: no hay ficheros entregados.

**Para decidir:** ¿esta línea te encaja? ¿Tienes un set (por ejemplo, de Agarimo) que quieras usar?

## 5. Estilo de fotografía

**Qué dicen las fuentes:** ya hay una sesión de estudio real (fondo gris liso, luz suave, ropa sencilla, poses naturales) de la que se han elegido 10 fotos. Agarimo pide frescura, modernidad y una imagen real, sin vender lo que no se es.

**Propuesta:** mantener esa línea: fotografía humana y natural, luz suave, fondo gris neutro que deje respirar el `violeta`; recortes cuadrados o verticales que sangran hasta el borde, sin filtros de color ni duotono; nada de stock genérico con apretones de manos.

**Para decidir:** ¿hay más fotos de la sesión que quieras añadir (primeros planos, detalle de pantalla)? ¿Aceptas retratos de clientes en testimonios y en qué formato?

## 6. Modo oscuro

**Qué dicen las fuentes:** Agarimo solo estudia el contraste sobre negro: el texto va en blanco; el violeta sobre negro es lo menos legible (3,67:1) y queda para gráficos como punto de luz; el gris `texto-secundario` sí funciona sobre negro (7,37:1). No hay diseño de modo oscuro para ninguna pieza.

**Propuesta:** un segundo tema `oscuro` con `fondo` en `negro`, `texto` en `blanco`, `texto-secundario` sin cambios, `acento` en `violeta` solo para gráficos y titulares de 24px o más, y `superficie` sustituido por un gris muy oscuro (a definir). Habría que decidir el gris y qué piezas lo usan.

**Para decidir:** ¿necesitas modo oscuro (web, posts, presentaciones)? Si sí, ¿en qué piezas?

## 7. Otros huecos detectados al montar los componentes

**Zona de respeto y tamaño mínimo del logotipo.** Las fuentes no los definen. Las maquetas lo usan entre 191px y 313px de ancho.

**Estados de interacción (hover, foco, enlace activo).** No vienen en las fuentes. Los componentes incluyen solo un contorno de foco negro de 2px, necesario para el teclado; el resto no se ha inventado.

**Medidas de la cabecera de la web** (alto, margen lateral, separación del menú): aproximadas. Las maquetas de Agarimo no dibujan la web.

**Para decidir:** ¿mínimo de ancho del logotipo y margen alrededor? ¿Quieres que la web tenga estados hover definidos?

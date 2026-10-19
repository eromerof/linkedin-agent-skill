Tres familias de botón, todas de esquinas rectas y sin sombra. Escribe el texto ya en MAYÚSCULAS.

- **Web principal** (`btn-primario`): relleno `violeta`, texto `blanco` (5,73:1), estilo `web-boton`, alto 60px. Medidas de la web: «CONTACTAR» 205×60px y «+ SOBRE LOS SERVICIOS» 324×60px. El prefijo «+ » marca un enlace secundario.
- **Web secundario** (`btn-secundario`): relleno `superficie`, texto `negro`, con flecha larga cuando lleva a otra página («VER SERVICIOS →»).
- **Posts**: botón de flecha 121×58px en `violeta` con flecha blanca (cierre de un post), y botones cuadrados de 129×129px para preguntas de sí o no: «SÍ» relleno violeta y «NO» con contorno negro de 2px.

Un botón por pieza. El principal es el que se quiere que se pulse; no pongas dos violetas juntos.

**Foco.** El contorno negro de 2px con separación de 3px al navegar con teclado es una adición mía: no sale en las fuentes y está pendiente de confirmar. No hay estado hover definido en las fuentes: no lo inventes.

La flecha es una línea de 2px con punta pequeña, dibujada a partir de las maquetas; no hay fichero de icono entregado (ver *Pendiente de definir*, iconografía).

```html
<a class="btn btn-primario web-boton" href="#">CONTACTAR</a>
```

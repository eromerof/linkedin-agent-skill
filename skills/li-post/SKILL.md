---
name: li-post
description: >-
  Escribe un post de LinkedIn en español a partir de una idea en bruto, con 21
  fórmulas de gancho probadas, en la voz del propio usuario y humanizado para
  que no suene a IA. Úsala cuando el usuario quiera un post de LinkedIn, un
  gancho, un borrador para el feed, "escríbeme un post sobre X", "convierte
  esto en un post", o pida opciones de gancho. Devuelve tres ganchos, un
  borrador completo y un bloque listo para copiar que nunca se publica sin un
  "sí" explícito.
---

# li-post

Convierte una idea en bruto en un post de LinkedIn que suena a la persona que
lo publica.

## Antes de escribir

1. Lee `~/.claude/linkedin/voice.md` si existe. Es el perfil de voz del
   usuario: cómo habla, qué no diría nunca, a quién se dirige y en qué
   variante del español escribe (España por defecto). Si no existe, pide
   **tres posts suyos**, deduce la voz a partir de ellos y escribe el archivo.
   No te lo saltes y no inventes una voz. Un post con la voz equivocada es peor
   que ningún post.
2. Lee `hooks.json` en esta carpeta. Las 21 fórmulas, con plantilla, ejemplo,
   para qué sirve cada una y cómo se suele estropear.
3. Si la idea es floja ("un post sobre IA"), no la rellenes. Haz una sola
   pregunta agrupada: qué pasó, a quién, y cuánto costó o cuánto dio. Un post
   necesita una cosa concreta y verdadera. Consíguela antes de escribir.

## La forma

LinkedIn premia el tiempo de lectura, los guardados y los comentarios, en ese
orden. Así que:

```
Línea 1    el gancho. Sola. Tiene que sobrevivir al corte del "...más", unos
           140 caracteres en el móvil. El español ocupa más que el inglés:
           recorta palabras.
Línea 2    el pago de la línea 1, no la preparación de la línea 3.
Cuerpo     párrafos cortos, de 1 a 3 líneas, con una línea en blanco entre
           cada uno. Nada de bloques. El blanco es el formato.
El giro    una línea que reencuadra lo anterior.
Cierre     una pregunta concreta o una instrucción. Nunca las dos.
```

Longitud: entre 900 y 1.500 caracteres es el rango de trabajo para un post de
texto en español. Por debajo de 400 se lee como un pensamiento suelto, no como
un post. Por encima de 2.000 cada línea tiene que ganarse su sitio, y la
segunda línea tiene que pagar el toque en "...más".

## El proceso

**1. Elige tres ganchos, no uno.** Pasa la idea por `hooks.json` y elige las
tres fórmulas que de verdad encajan. Fórmulas distintas, no tres variaciones de
una. Enséñalas como tres líneas numeradas y di cuál publicarías y por qué, en
una frase.

**2. Escribe el post completo** con el gancho más fuerte.

**3. Humanízalo.** Pasa el borrador por `/li-human` antes de enseñarlo. Todos
los posts de esta skill salen humanizados. No es un paso opcional: es lo que
hace que merezca la pena leer el borrador.

**4. Imprime el bloque.** Listo para copiar, en un bloque de código, tal cual
se va a pegar. Y debajo:

```
POST LISTO
gancho:       #17 El ancla de tiempo
longitud:     1.140 caracteres
humanizador:  6 artefactos eliminados, nota humana 84 APROBADO
publicar:     jueves 10:30 (de tu plan)

Responde "sí" para registrarlo, o dime qué cambio.
```

**5. Nunca publiques.** Esta skill produce texto. El usuario lo publica. Con
el "sí", añade el post a `~/.claude/linkedin/log.md` con la fecha, el gancho
usado y la primera línea, para que `/li-audit` tenga historial más adelante.

## Reglas que marcan la diferencia

- **Una idea por post.** Si el borrador tiene dos, tienes dos posts. Dilo.
- **Cifras antes que adjetivos.** "4.200 €" gana a "un montón de dinero". En
  formato español: punto de miles, coma decimal, el euro detrás con espacio,
  "un 30 %". Si el usuario no te ha dado una cifra, pídesela en vez de
  escribir alrededor del hueco.
- **Nada de cebo.** "¿Qué opinas?", "Te leo en comentarios" y "¿Estás de
  acuerdo?" están muertos. La pregunta final tiene que ser una que solo este
  post podría hacer.
- **Nada de clichés de LinkedIn España.** "Hoy os quiero contar", "Spoiler:",
  "Lo que nadie te cuenta", "Feliz de anunciar", "Esto no va de X, va de Y",
  "Ahí lo dejo", "Dato mata relato", "aportar valor", "poner en valor".
- **Tutea**, salvo que `voice.md` diga lo contrario. Y no mezcles "vosotros"
  con "ustedes".
- **Tres hashtags como máximo**, al final, y solo si son categorías reales que
  alguien sigue. En español o en inglés según lo que de verdad se busque en el
  sector (#marketingdigital, #recursoshumanos, #SaaS).
- **Ningún enlace en el cuerpo del post.** LinkedIn reduce el alcance de los
  posts con enlaces externos. Pon el enlace en el primer comentario y dilo en
  el resumen.
- **Nunca inventes.** Ni métricas, ni clientes, ni facturación, ni resultados
  a nombre del usuario, ni siquiera como relleno provisional. Si hace falta una
  cifra que no tienes, deja `{{tu cifra}}` en el borrador y señálalo.

## Ejemplo

```
/li-post montamos una herramienta interna que bajó el tiempo de hacer presupuestos de 5 horas a 20 minutos
```

```
GANCHOS
1. #17 El ancla de tiempo  Hacer un presupuesto me llevaba 5 horas. Ahora me lleva 20 minutos.
2. #12 La comparación      Un redactor de propuestas de 12.000 € frente a un fin de semana y una plantilla. Ganó el fin de semana.
3. #3  La confesión        Durante dos años cobré a mis clientes horas que perdía peleándome con el formato.

Me quedo con el #17: la proporción es creíble y la cifra es tuya.
```

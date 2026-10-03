# Hacer una web GYF

**Protocolo interno de El Gordo y el Flaco · v11 · 3 de octubre de 2026**

Un solo protocolo para los dos encargos de la agencia: **la web de un cliente que no tiene** y
**la web de un cliente que tiene una y hay que rehacerla** porque no le sirve para sus objetivos.

Destilado de **Marcos Cerrajeros** (9-22 de septiembre), **Balgas** (23-26 de septiembre, primera
web hecha con el método de principio a fin), **la web propia de El Gordo y el Flaco** (26-27 de
septiembre), **Vinos Gallegos Pousada** (28 de septiembre, arranque) y **Solvento** (29 de septiembre
a 3 de octubre: una v1 que pasó todos los controles y aun así «cojeaba» por el contenido, la
plantilla y el movimiento, y una v2 rehecha en una noche). Sustituye a la v10 y a todas las anteriores.

**Qué cambia en la v11, en una línea:** el protocolo ya no solo dice cómo se hace una web, sino
**cómo se ve que cojea y qué paso la arregla** (el detector), y cierra los cuatro agujeros por los que
se coló Solvento: contenido que no se juzgaba contra el objetivo, promesas comerciales sin validar,
piezas elegidas solo de una plantilla y agentes que figuraban sin haber trabajado.

---

## Para qué sirve

Que a partir de la investigación previa del cliente salga una web propia, distinta de las demás,
con la riqueza visual de una plantilla de primera y lista para posicionar, y que Álvaro solo tenga
que intervenir en tres momentos. Lo que se repite en cada cliente vive en el **sistema** (paso
cero); lo que depende de esperar al cliente va **en paralelo**; lo que se puede comprobar a
máquina, se comprueba a máquina; y **nada llega a GitHub con una duda abierta**.

**El protocolo tiene la solución dentro.** Cuando una web cojea, el fallo es de una de dos cosas:
o un paso no se hizo como dice, o el protocolo no lo prevé. Lo primero se arregla volviendo a ese
paso; lo segundo, con una línea en `CAMBIOS-PARA-PROTOCOLO-v<N+1>.md` el mismo día y una fila
nueva en el detector en la versión siguiente. Nunca con veinte retoques sueltos.

**Aviso honesto sobre los plazos:** el plazo real es de **tres o cuatro días de trabajo**: medio día
para la plantilla nueva (B1-B10), uno para
contenido y fotos, uno para construir y controlar, y lo que tarde el cliente en contestar.

---

## Cómo se usa

**48 pasos numerados de corrido** (con algunos «b» intercalados). Se trabaja diciendo «vamos con el
12», «el 12 está hecho». Un paso se cierra cuando se puede enseñar el resultado, no cuando se ha
entendido.

**Dos marcas:**
- **[E]** · solo si el cliente **ya tiene web** (hay que sustituirla).
- **[N]** · solo si la web es **nueva** (el cliente no tiene).
- Sin marca, vale para los dos. La numeración no cambia: el paso que no toca se salta.

**Cada paso dice quién lo hace** (columna «Quién»). Si es un agente, **se invoca de verdad** con su
skill (o como subagente con su skill) y su informe se guarda en la carpeta del cliente. En `ESTADO.md`
hay un **registro de agentes**: paso, agente, fecha, cómo se invocó y dónde está el informe. Si
Claude hace un paso de agente sin invocarlo (por el límite de uso o por prisa), lo apunta como
**«sin agente: lo hizo Claude»** y lo dice. Nunca se firma un documento con el nombre de un agente
que no ha trabajado (en Solvento, la ficha de firma decía «Jean Paul» y «Merche reescribió» sin que
ninguno se hubiera invocado; Álvaro lo preguntó y no había respuesta buena).

**ESTADO.md.** Cada proyecto de cliente tiene su `ESTADO.md`: caso (E o N), paso en curso,
decisiones, pendientes y el registro de agentes. Cada conversación empieza leyendo este protocolo y
`ESTADO.md` y diciendo en qué paso está. **Al cerrar cada paso se guarda en los dos sitios: la
carpeta del cliente y el proyecto.**

**Traspaso entre conversaciones.** Cuando una conversación se hace larga o Álvaro se acerca a su
límite de uso, se sigue en una conversación nueva con `TRASPASO.md`, **guardado en el proyecto y en la
carpeta antes de cerrar** (en Pousada, el traspaso pegado en el chat llegó cortado dos veces): en el
chat nuevo solo se escribe «lee TRASPASO.md». Lleva arriba una **sección 0, «pendiente de aplicar»**.
**Lo que solo vive en la nube de una sesión se pierde al cerrarla**: el repositorio con su historial
y las imágenes que Álvaro pega en el chat. Por eso, al cerrar cada versión, la copia completa del
repositorio va a la carpeta (`08-WEB/REPOSITORIO-vN/`), y cada imagen y cada informe (Search Console,
auditorías) se guarda en la carpeta **en el momento en que llega**.

**El límite de uso se dice como lo que es:** «lo dejamos para cuando se renueve tu límite», nunca
«hasta el viernes no se puede».

**El estado, en grupos de pasos.** Cuando Álvaro pide «¿cómo vamos?», la respuesta va por fases,
con lo cerrado, lo que falta y quién lo tiene, y un número: pasos cerrados de 48.

**Tres momentos para Álvaro** (✋), más **una pregunta y una lista** al principio. Todo lo demás lo
decide Claude y lo deja por escrito en `ESTADO.md`, donde Álvaro puede revocarlo:

0. **Paso 2b** · valida la **lista de promesas** (qué se puede prometer y qué no). **Paso 20** · dice
   el **nivel de movimiento** que quiere (quieto, medio o «como GYF»). Son dos respuestas cortas que
   ahorran una web entera.
1. **Paso 22** · da el visto bueno a la dirección visual (con maqueta completa delante). Puede
   **delegarlo entero** en Jean Paul.
2. **Paso 33** · da por buena la web después de la prueba con personas.
3. **Paso 38** · da la orden de publicar.

**Cuando Álvaro corrige algo, lo primero es el detector** (ver «El detector», al final de los
pasos): se busca la fila del síntoma, se vuelve al paso que la arregla y se aplica a **toda** la web,
no solo a la página que señaló. Si no hay fila, es una trampa nueva: línea en `CAMBIOS-…` en el acto.

**Cómo se habla con Álvaro.** De tú. Corto: la respuesta y, si hace falta, una línea de contexto.
Sin anglicismos ni emojis. Lo que se sabe se separa de lo que se supone. Cuando pide conversar, un
párrafo por un párrafo. Cuando escribe «h» durante una tanda de descargas, es «hecho».

| Cuándo | Pasos | Qué sale |
|---|---|---|
| Día 0 | 1 – 4 | Investigación, lista de promesas, datos de la ficha, **preguntas y encargo de fotos al cliente** |
| Día 1 | 5 – 19 | Diagnóstico, terreno, contenido completo juzgado contra el objetivo y fotos (en paralelo) |
| Día 2 | 20 – 22 | Plantilla y nivel de movimiento, ficha de firma desde el catálogo y maqueta completa ✋ |
| Día 3 | 23 – 37 | Construcción, controles, detector, prueba con personas y auditoría |
| Cuando diga Álvaro | 38 – 48 | Publicar y todo lo que depende de la web publicada |

| Fase | Pasos | Qué se resuelve |
|---|---|---|
| 00 · Arranque | 1 – 4 | Qué quiere el cliente, qué se le puede prometer y qué hace falta de él |
| 01 · Diagnóstico | 5 – 7 | Qué hay y qué no se puede romper |
| 02 · Congelar el terreno **[E]** | 8 – 9 | Que el cambio no cueste posiciones |
| 03 · Contenido | 10 – 15 | Keywords, enlaces y todos los textos, juzgados contra el objetivo y sin una duda abierta |
| 04 · Fotos | 16 – 18 | El techo real de calidad |
| 05 · Identidad | 19 | La marca como recurso gráfico |
| 06 · Firma gráfica | 20 – 22 | Que la web sea «de su padre y de su madre» y tenga la gracia que se pidió ✋ |
| 07 · Construir | 23 – 27 | La web, generada a máquina y entregada en tandas que GitHub acepta |
| 08 · Controlar | 28 – 31b | Que ningún defecto llegue a nadie (controles, Lighthouse y detector) |
| 09 · Prueba con personas | 32 – 33 | Lo que ven los de fuera ✋ |
| 10 · Auditar | 34 – 37 | Seis especialistas, invocados de verdad, arreglo y reauditoría |
| 11 · Publicar | 38 – 42 | El cambio en un solo movimiento ✋ |
| 12 · Después | 43 – 48 | Conectar, medir y cerrar |

---

## El equipo: quién participa en cada fase

Claude coordina y ejecuta. Cada agente entra **invocado con su skill** en el paso que le toca; cuando
hay varios a la vez, se lanzan **en paralelo y sin ver el trabajo de los demás**, en tandas de dos o
tres como mucho (en Solvento, cuatro a la vez agotaron el límite semanal y el cuarto no dejó nada), y
cada informe se guarda en la carpeta en cuanto llega. En clientes dentales, **Marta** sustituye a Jean
Paul y **Lorena** a Merche.

| Agente | Qué hace en una web | Pasos |
|---|---|---|
| **Jean Pierre** (dirección) | Convierte la investigación previa en argumentario, **lector principal** y **lista de promesas** | 2 · 2b |
| **Matías** (SEO local) | Audita la ficha de Google y da los planos de SEO local; luego audita la web | 5 · 11 · 34 |
| **Bruno** (SEO técnico) | Audita la web actual y la nueva: indexación, rendimiento, schema, `.htaccess` | 5 · 8 · 34 · 41 |
| **Iñaki** (datos) | Foto de partida (Search Console, ficha) y medición a 2, 6 y 12 semanas | 9 · 48 |
| **Nuria** (keywords) | Keywords y arquitectura de páginas, sin canibalización | 11 |
| **Turing** (IA) | Que el cliente salga en ChatGPT, Perplexity y AI Overviews; perfiles externos; audita | 5 · 11 · 34 |
| **Merche** (copy) | Escribe todos los textos con la voz del cliente; **juzga el contenido contra el objetivo**; audita el copy | 13 · 15 · 34 |
| **Jack** (plantillas) | Busca tres plantillas o propone las de la biblioteca, y destripa la elegida (B1-B9) | 20 |
| **Jean Paul** (diseño) | Dirige el arte, **escribe la ficha de firma desde el catálogo**, decide lo que Álvaro le delega; audita el diseño | 16 · 19 · 21 · 22 · 34 |
| **Dani** (CRO) | Decide dónde y cómo convierte cada página; **la tabla de llamadas a la acción**; juzga el contenido con Merche; audita | 15 · 21 · 34 |
| **Kubrick** (movimiento) | Monta la capa de movimiento según el nivel pedido | 21 · 25 |
| **Emil** (microinteracciones) | Revisa hover, transiciones y curvas antes de enseñar la web | 31b |
| **Imagen de marca GYF** | Pone la marca de la agencia a todo documento que se entrega (PDF, Word) | Cuando se entrega un documento |
| **Demiurgo** | Mete en los skills lo que se ha aprendido en la web | 48 |

---

## Los principios

> **1. La web vieja sigue viva hasta el último minuto [E].** La nueva se construye entera en
> paralelo, se verifica entera y solo entonces se cambia.

> **2. Si el objetivo no cambia, se conservan las URLs; si cambia, se rehace todo con 301 [E].**
> Objetivo nuevo: arquitectura, URLs, keywords y textos nuevos, y las URLs viejas con impresiones
> van con **301 de un solo salto**.

> **3. Manda la ficha de Google.** Ante cualquier discrepancia de datos gana lo que dice la ficha.
> No se añade ningún dato que la ficha no tenga.

> **4. Nada inventado.** Ni reseñas, ni cifras, ni **promesas que no estén en la lista del paso 2b**,
> ni datos de un municipio que no se hayan comprobado en una fuente oficial.

> **5. Cada web, «de su padre y de su madre».** Qué movimiento, qué fondos y qué capas sale de la
> plantilla, del catálogo de piezas y del motivo del cliente, nunca de copiar la web anterior.

> **6. La plantilla se traslada, no se interpreta… ni se adelgaza.** Lo que el cliente rechaza (una
> foto, un objeto) se **sustituye por algo del mismo peso visual**, nunca se deja el hueco en blanco.

> **7. La web es de la marca.** El nombre de la persona va en los legales y, como mucho, en contacto.
> Nunca se destacan recuentos pequeños.

> **8. La web se escribe para un lector y para una decisión.** Cada página sabe quién la lee
> (en Solvento, el administrador de fincas) y qué tiene que decidir al terminarla. Lo que habla a
> otro público sale del menú y va al pie. Un texto correcto que no le da al lector lo que necesita
> para decidir es un texto que falla, aunque pase todos los controles.

> **9. Cada llamada a la acción responde a la pregunta que tiene el lector en ese punto.** Si la
> pregunta es «¿busco una empresa seria?», la respuesta es «Llámenos», no «Mándenos una foto».

---

## El stack y la entrega

- **GitHub** guarda el repositorio del cliente (código, generador y `sitio/`). **git no se usa dentro
  de las carpetas conectadas** (sin permiso de borrado deja `HEAD.lock` y temporales): el repositorio
  lo crea Álvaro en GitHub y se sube por la web.
- **Vercel** sirve la **vista previa** (`*.vercel.app`), que **nunca se indexa**. **Alta del proyecto,
  la primera vez (en Solvento salió un 404 por esto):** importar el repositorio, **Root Directory =
  `sitio`** (en «Settings → Build and Deployment», o al importar en «Edit» junto a Root Directory),
  Framework «Other», sin comando de build. `vercel.json` con el `noindex` va en `sitio/`.
- **El hosting del cliente** sirve la web de producción. Se sube una vez, terminada y aprobada.

**Cómo se entrega cada versión** (Álvaro sube por la web de GitHub):
- `08-WEB/SUBIR-A-GITHUB/<cliente>-vN-tandaN.zip` (o la carpeta `vN-CAMBIOS/TANDA-n`): **solo los
  archivos que cambian**, con el árbol del repositorio, en tandas de **menos de 100 archivos y menos de
  25 MB**. Las hace `herramientas/entrega.py`, que **comprueba los dos límites y se para si no se
  cumplen**. La primera entrega de un repositorio nuevo va entera en tandas.
- `08-WEB/repositorio-vN/`: la copia completa y al día (de trabajo; no se sube).
- `08-WEB/LEEME.txt` con el orden de arrastre. **Se arrastran las carpetas que se ven al abrir la
  TANDA, juntas, nunca lo que hay dentro de ellas.**
- Lo sustituido va a `_to_delete/`. **Claude pide el permiso de borrado al empezar la sesión** (para la
  prueba de arranque y para vaciar `_to_delete/` al cerrar la versión). Fuera de `_to_delete/` no se
  borra nada.
- **Si Álvaro todavía no ha subido una tanda y llegan retoques, se rehace esa misma tanda.**
- **Solo cuentan los archivos cuyo contenido cambia** (`git config core.fileMode false`).
- **Paso de archivos entre la nube y la carpeta:** como mucho 20 MB por archivo; se envía con el
  identificador del archivo, nunca por ruta, y **se comprueba el tamaño al otro lado**.
- **Retomar el repositorio en una sesión nueva:** subir `08-WEB/REPOSITORIO-vN/` a la nube, `git init`,
  `core.fileMode false`, y `build.py` → `rematar.py` → `controles.py` para comprobar que sale igual.
- GitHub **no sube archivos que empiezan por punto** (`.htaccess`): va al hosting el día de publicar.

**Carpeta del cliente**, siempre igual:
`00-…` (auditorías de partida) · `01-TEXTOS-ANTIGUOS` [E] · `02-KEYWORDS-Y-ARQUITECTURA` ·
`03-FOTOS` (`00-PLAN-Y-PROMPTS`, `01-ORIGINALES`, `02-SE-SALVA`, `03-GENERADAS`, `04-FOTOS-WEB`,
`06-CASOS`, `07-FOTOS-ARTISTICAS`) · `04-LEGALES` · `05-TEXTOS-NUEVOS` · `06-IMAGEN-DE-MARCA` ·
`07-FIRMA-GRAFICA` · `08-WEB` · `09-AUDITORIA` · `_to_delete` · y en la raíz `ESTADO.md`,
`PROMESAS.md` y `CAMBIOS-PARA-PROTOCOLO-v<N+1>.md`.

---

# PASO CERO · EL SISTEMA

*No se repite en cada cliente. Vive en el proyecto del sistema GYF, nunca en el de un cliente.*

## A · La base GYF (repositorio plantilla)

Cada web nace del tema de su plantilla (ver B), que lleva dentro esta base, probada en Balgas, GYF y
Solvento:

| Pieza | Qué es |
|---|---|
| Generador | `contenido/paginas/*.md` → `sitio/`. Orden fijo: `build.py`, `rematar.py` (siempre el último) y `controles.py`. La home también se genera |
| `base.css` + tema | CSS propio de la agencia más el tema de la plantilla |
| `controles.py` | Estructura y SEO de cada página, contrato de enlaces, sitemap, controles de texto y de fotos y **promesas** (paso 28) |
| Cabecera | **Siempre a la vista**: al bajar se compacta y toma fondo, pero no se esconde. **El logo, con el alto medido contra la demo** (en Solvento salió pequeño) |
| Tarjeta de conversión | Estado en vivo con el horario de la ficha (y festivos), nota de Google, «¿Prefiere que le llamemos?» |
| `enviar.php` | Formulario de llamada y de contacto en el mismo archivo, con trampa y tiempo mínimo, sin captcha; **admite adjuntos** si el formulario lleva fotos |
| `resenas.json` | Nota y opiniones reales. **Se sacan desde la vista del propietario** (paso 3). Se cambia en GitHub y actualiza tarjeta, contadores y opiniones. **El número de reseñas solo se enseña si el cliente quiere** (`NOTA_CON_NUMERO`) |
| Opiniones | 7-11 reseñas reales, tarjetas iguales 4:5 con «Leer más», botón a la ficha por su CID |
| Opiniones por página | Cada página ordena las reseñas por su tema y pone **una cita literal** elegida a mano; el generador comprueba que es literal |
| **Pie por página** | `PIE_FRASES` en `config.py`: por URL, antetítulo (la pregunta del lector), titular (la respuesta), subtítulo y orden de botones. Sin frase propia sale la de defecto y `controles.py` avisa |
| **Marcadores del texto** | Fijos y reconocidos por el tema: `(FOTO: descripción — archivo.jpg)`, `(Bloque de opiniones… n.º X… Fragmento literal: «…»)`, `(Mapa de Google…)`, «**Formulario:**», «[Botón]», «Línea informativa», «Etiqueta:», «Entrada corta:», **«Lector:»** y **«Decide:»** |
| Preguntas frecuentes | Acordeón numerado, una abierta cada vez |
| Botones | El texto va **una sola vez** en el HTML; `main.js` lo parte en letras solo con ratón |
| Cortinilla | Solo tras un clic interno, nunca al entrar desde Google |
| Largo de la home | Unas **20 pantallas en escritorio como mucho**. En el móvil, servicios, pasos y equipo en carrusel horizontal |
| Festivos | Los de Pascua se calculan; los fijados con año **se revisan antes del 1 de enero** |
| Casos | Composiciones con capturas reales en portátil y móvil (`herramientas/maquetas/`). Cada trabajo lleva **varias categorías** (`CASOS_CATEGORIAS`) |
| Muestra de trabajos | En «Quiénes somos», **cada trabajo que se nombra lleva su maqueta** (`MUESTRA_FOTO`); la rejilla, en múltiplos de 2 y de 3 |
| Caso sin web | Enlace «Ver la ficha» a su ficha de Google (`CASOS_VER_CASO`). Se da **el municipio real del local**; en la página de otro municipio sale como «El caso más cercano» |
| Tira de logotipos | Clientes en gris que pasan a su color; orden en `logos.json`; **múltiplos de 6** |
| Huecos de foto | Encuadre y marcador de la marca mientras no llega la foto |
| Schema | LocalBusiness concreto con `geo`, `hasMap` y `sameAs` comprobados, WebPage, WebSite, BreadcrumbList, Service y FAQPage |
| SEO técnico | Canónicas, `sitemap.xml` con `lastmod`, `robots.txt`, Open Graph por página, `llms.txt` |
| `.htaccess` | Sin www, https con `X-Forwarded-Proto`, 410, 301 de un solo salto (desde `mapa301.json`), bloqueos, caché, compresión y MIME |
| `vercel.json` | `noindex` en toda la vista previa |
| Medición | GTM heredado, solo en el dominio real y con consentimiento |
| Rendimiento | GSAP, ScrollTrigger y Lenis alojados y cargados al terminar la carga; 3D diferido con imagen fija como LCP; sin JS o con movimiento reducido, todo quieto y completo. **En pantallas táctiles, nada con scrub de texto** (R11 bajaba el contraste en el móvil) |
| Herramientas | `servir.sh`, `capturas.py`, `control29.py`, `lighthouse.sh`, `entrega.py` (tandas con límites) y `maquetas.py` |

**Avisos comerciales:** la web es estática, así que el cliente no tiene editor (salvo
`resenas.json`). Se dice antes de vender.

## B · La biblioteca de plantillas y el catálogo de piezas

La biblioteca guarda cada plantilla estudiada como **ficha + variaciones + tema en código**
(`000-BIBLIOTECA PLANTILLAS/00N-NOMBRE/`), y desde la v11 tiene además el **catálogo de piezas**
(`CATALOGO-DE-PIEZAS.md` + `CATALOGO/capturas/`): **todas las piezas de todas las plantillas y de todas
las webs hechas**, ordenadas por zona de la página (portada, al bajar, texto, servicios, fotos,
secciones clavadas, cifras, objetos, bandas, pie, cabecera, conversión, lectura), con qué cura cada
una, de dónde sale, **si ya está en código y dónde**, en qué webs se usó y su captura. Empieza con una
tabla «del síntoma a la pieza».

**Para qué:** que una web no dependa de la plantilla que le tocó. En Solvento, la v1 se hizo solo con
lo que traía Archidex y salió sosa; la v2 cogió piezas de Rayo y de GYF e hizo dos nuevas (el paso a
paso clavado y el pie por página), que ahora están en el catálogo para la siguiente.

**Regla de plantilla (Álvaro, 03/10/2026; vale hasta nuevo aviso):**
1. **Primero, siempre, una plantilla nueva**: Jack busca tres en ThemeForest, elige Álvaro y Jack la
   destripa (B1-B10). Objetivo: llegar a **12-15 plantillas** que nos gusten y hagan el trabajo
   interesante. La tabla de B1.5 lleva **tres plantillas nuevas**, nunca una de la biblioteca.
2. **Solo si el resultado no funciona** (la maqueta del 21 o la web construida cojea en el detector:
   sosa, sin el nivel de movimiento pedido, sin golpe), **se recurre a la biblioteca y al catálogo**
   para sacar piezas que hagan la web más competitiva, y si hace falta se cambia de base a una
   plantilla de la biblioteca con tema en código, **cambiando las seis piezas** de su `VARIACIONES.md`.
   Así fue Solvento: Archidex (nueva) salió sosa y la v2 tiró de Rayo y del catálogo.
3. La biblioteca sigue creciendo: cada web **aporta al catálogo** sus piezas nuevas (paso 48).

| Nº | Paso |
|---|---|
| B1 | **Buscar**: ranking real de ThemeForest. Se elige por **calidad y flexibilidad, nunca por sector**. Filtro: nota ≥ 4,5 con 20 votos o más; **para las de menos de 12 meses, más de 100 ventas, nota ≥ 4,8 y autor con historial** (con el filtro viejo solo pasaban plantillas de 2015-2017). Si la demo no se deja abrir fuera de ThemeForest, se dice en la tabla |
| B2 | Entrar al **dominio real de la demo** y elegir la página que se va a trasladar |
| B3 | **Tokens por anchos**, con JavaScript sobre la demo a 1.440, 768 y 375 px |
| B4 | **Inventario de secciones** en orden |
| B5 | **La portada, tal cual**, en escritorio y en móvil |
| B6 | **Índice de efectos del código** |
| B7 | **Fotos y visuales, uno a uno**, y qué pone la plantilla en cada hueco |
| B8 | **Conversión y lo que no se copia** |
| B9 | **Capturas** a los tres anchos (forzando `main{opacity:1}` en plantillas que lo esconden hasta el JS; zoom de Chrome sobre el iframe para 1 px por píxel) |
| B10 | **Escribir el tema** y probarlo con un cliente de ejemplo. **Con prisa, se puede escribir directamente en el repositorio del cliente** y llevarlo a la biblioteca en el paso 48 (el `ESTADO.md` de la entrada lo dice: «A medias: el código vive en <cliente>») |
| B11 | **Pasar sus piezas al catálogo**: una fila por efecto que se vaya a poder usar, con su captura |

**Entradas (03/10/2026):** 001 Crafto · 002 GYF-Orisa (Balgas, con tema) · 003 Rayo (GYF y Solvento
v2, con tema) · 004 AJÁ · 005 Arctiq (Marcos) · 006 Tank (Pousada) · 007 Archidex (Solvento v1, tema en
el cliente).

---

# LOS 48 PASOS

## Fase 00 · Arranque (día 0)

| Nº | Paso | Quién |
|---|---|---|
| 1 | **Antes de nada, comprobar el sistema:** que los cuatro archivos del sistema están en el proyecto (en Solvento se trabajó un día sin ellos) y que la copia de `03-BIBLIOTECA-LEEME.md` es la del `LEEME.md` de la biblioteca (estaba desfasada). Pedir el **permiso de borrado** de la carpeta. Abrir la carpeta con la estructura fija y crear `ESTADO.md` (carpeta **y** proyecto) con el registro de agentes vacío. Declarar el caso: **E** o **N**; **[E]** si el objetivo se mantiene o cambia. **Comparar el NAP de la ficha con el de la web vieja** el primer día (en Solvento, la ficha decía Leganés y la web Alcorcón) | Claude |
| 2 | **Investigación previa del cliente** (la aporta Álvaro): de ahí salen el **argumentario**, la **voz** (tú o usted), el **lector principal** de la web y los secundarios, y **qué tiene que decidir** cada lector (llamar, pedir visita, mandar datos). **El lector principal manda en todo**: arquitectura, menú, textos y llamadas. Se apunta en `ESTADO.md`. Además, el **inventario de datos del cliente**: cada cifra, credencial, inversión o diferencia que se sepa (en Solvento: 20 administradores, la cabina de 10.000 €, el RERA, el seguro de 1,3 M€). Ese inventario se usa entero o se descarta a sabiendas en el paso 15 | Jean Pierre |
| 2b | ✋ **Lista de promesas** (`PROMESAS.md`): qué se puede decir sobre **plazos, presupuestos, visitas, garantías, urgencias, horarios, precios y para qué sirve cada cosa que se le pide al lector** (una foto, un formulario). Dos columnas: **se puede decir** y **no se dice nunca**, con la frase exacta. **Álvaro la valida antes de escribir una línea.** Lo que no está en la lista no se promete: va como ⚑. (En Solvento se publicó «presupuesto con una foto» por toda la web y la foto solo sirve para orientarse; y «atención rápida» chocaba con «no hacemos urgencias») | Jean Pierre · Álvaro |
| 3 | **Datos de la ficha de Google**: nombre, dirección, teléfono, horario, categoría, nota, número de reseñas, **CID y el ID del negocio del panel**. **Sacar TODAS las reseñas reales, literales, a `resenas.json`, desde la vista del propietario** (`google.com/local/business/<id>/customers/reviews`; en Maps solo cargaban 9 de 61). Estos datos mandan en todo lo demás | Claude |
| 4 | **Una sola tanda de preguntas al cliente**, con el encargo de fotos reales y la petición de reseñas que digan el pueblo y el servicio. **Antes de preguntar, se busca en la carpeta del cliente, en la web actual y en lo que tenga Álvaro** (en Solvento se pidió un dato que tenía Álvaro). **Una tanda y, como mucho, una de aclaraciones de 3-4 preguntas** (a Isra se le cansó con tres). **Se pregunta con qué abre los archivos** (iPad: el Excel va como `.numbers` o PDF). La lista fija de la casa: horario real · cuánto tarda en devolver una llamada · año de inicio · medios de pago · garantía · **lista cerrada de municipios** · acreditaciones · festivos locales · titular legal y NIF · WhatsApp · visita o auditoría gratis · **qué no hace, y qué sí hace aunque no lo anuncie** · **qué no promete nunca** (completa el 2b) · casos con nombre · logotipos de clientes · equipo · si sale en fotos · perfiles de redes de la marca | Claude |

## Fase 01 · Diagnóstico (día 1, en paralelo)

| Nº | Paso | Quién |
|---|---|---|
| 5 | Auditoría de la ficha, **[E]** de la web actual y de los **perfiles externos**. `sameAs` solo con perfiles de la marca comprobados. **En dos tandas** (Matías y Bruno; después Turing) y cada informe a la carpeta en cuanto llega | Matías · Bruno · Turing |
| 6 | **[E]** Inventario del hosting y que el buzón del formulario existe y se lee. **[N]** Dónde se publica | Claude |
| 7 | **Medición heredada**: GTM, etiquetas y conversiones de Ads **[E]**; o qué hay que crear **[N]** | Claude |

## Fase 02 · Congelar el terreno [E] (siempre ANTES de la arquitectura)

| Nº | Paso | Quién |
|---|---|---|
| 8 | **[E]** Lista exacta de URLs del sitemap **y de todas las que tengan impresiones en Search Console**. **www o sin www**. Mapa de 301 (un solo salto) y 410 en `mapa301.json` | Bruno |
| 9 | **[E]** **Foto de partida** con fecha, **guardada en `00-AUDITORIAS` en el momento** (`.md` + `.csv`; en Pousada se perdió en el chat). De Search Console: todas las URLs y, de consultas, las que tienen clics, las de más impresiones sin clic y un filtro por el objetivo (la herramienta corta hacia las 1.000 filas) | Iñaki |

**Los pasos 8-9 van antes del 11, sin excepción.**

## Fase 03 · Contenido

| Nº | Paso | Quién |
|---|---|---|
| 10 | **[E]** Vaciar la web vieja: textos con sus enlaces, **todas las fotos** y los legales | Claude |
| 11 | **Keywords y arquitectura**: keyword principal y secundarias por página, **para el lector principal del paso 2**. **Negocio de barrio**: su municipio primero, después los de alrededor; «Madrid» no interesa. **Distribuidor o servicio a empresas** (Pousada, Solvento con administradores): la ciudad o la zona que atiende es la zona, aunque el local esté en otro municipio. **Los lectores secundarios no van en el menú**: van al pie (en Solvento, los particulares). **[E] con objetivo nuevo**: arquitectura desde cero y 301 | Nuria (con Matías y Turing) |
| 12 | **Contrato de enlaces**: bloques repetidos una vez; enlaces editoriales página a página | Claude |
| 13 | **Escribir cada página** (`contenido/paginas/NN_nombre.md`) con la voz del paso 2, las keywords del 11, los enlaces del 12 y **los marcadores fijos de la base**. Cada página empieza con **«Lector:»** y **«Decide:»** (no se publican: los lee el control y el paso 15). H1 de 3 líneas como mucho en móvil; title ≤ 60 caracteres. Primer párrafo ≤ 60 palabras, autosuficiente y citable. Dos o tres H2 en forma de pregunta. **Lo importante para decidir va en la página del servicio, no en la de preguntas** (en Solvento, la v1 dejaba lo legal y lo económico del amianto en la FAQ). **Toda promesa sale literal de `PROMESAS.md`**; toda frase en negativo sobre un servicio, toda afirmación sobre cómo trabaja el cliente y todo dato de un municipio se marcan ⚑ hasta que se confirmen. **El pie de cada página** (`PIE_FRASES`): la pregunta que tiene ese lector al terminar, la respuesta y la acción que le corresponde (principio 9) | Merche |
| 14 | **Formularios sin casilla de privacidad** (línea informativa y art. 6.1.b RGPD). **Legales**: **[E]** se corrigen con la ficha; **[N]** los de la base. **Si el formulario pide fotos, la línea dice para qué sirven, con la frase de `PROMESAS.md`** | Claude |
| 15 | **Cierre del contenido: cero ⚑ y el contenido juzgado contra el objetivo.** (a) Claude comprueba citas contra `resenas.json` y entidades de municipio solo con fuente oficial. (b) Lo demás va al cliente en **una sola tanda**. (c) Controles de texto del paso 28. (d) **Juicio contra el objetivo** (Merche y Dani, invocados, sin verse): página a página, **«¿tiene este lector lo que necesita para decidir?»**, con una **lista de huecos por página**; y el **inventario de datos del paso 2**: cada dato está usado en la página donde decide, o descartado con su motivo. Se compara con la competencia que vio Jean Pierre: si ellos explican algo que nosotros no, es un hueco. (e) **Promesas**: ninguna frase promete algo que no esté en `PROMESAS.md` (lo cuenta también el control). (f) **Detector, filas de contenido** (ver «El detector»). La aprobación del cliente no es obligatoria: decide Álvaro | Merche · Dani · Claude |

**Lo que se elimina siempre de los textos:** 24 horas, urgencias o fines de semana que no son
verdad, precios, «equipo de técnicos» si es una persona, fechas que caducan, frases de relleno de
agencia, los tics de texto escrito por IA, **cualquier recuento pequeño** y **cualquier promesa fuera
de la lista**.

## Fase 04 · Fotos (en paralelo desde el paso 11)

| Nº | Paso | Quién |
|---|---|---|
| 16 | **[E]** Inventario de las fotos viejas. **Plan de visuales por hueco de la plantilla y del catálogo.** Nombre de archivo = keyword + localidad. **La portada lleva visuales propios** (objeto 3D, casos reales, foto real del cliente), **no fotos de Gemini, salvo decisión expresa de Álvaro**, que se apunta en la ficha de firma y en `ESTADO.md` (en Solvento se aceptó para la galería). Los casos: capturas **HD de escritorio que hace Álvaro** (1.920 de ancho, o DevTools a 1.440 × 909 con DPR 2) en `03-FOTOS/06-CASOS/crudo-hd/`, montadas con `maquetas.py`, que recorta lo que no es la web (`RECORTE_HD`) y renderiza con `html{zoom:3}`. **Fotos de la ficha con datos viejos** (un móvil antiguo en una lona) se recortan sin esa parte | Jean Paul |
| 17 | **Generar con Gemini** fotos **artísticas, de tema, no de banco**, una conversación por foto, hoja de contactos antes de bajar. **No se descargan una a una desde Chrome** (solo deja bajar la primera): Álvaro las baja todas juntas desde la Biblioteca de Gemini a `E:\01-DESCARGAS` y Claude las identifica con una hoja de contactos y les pone su nombre | Claude · Álvaro |
| 18 | **Revisar y procesar.** Sin duplicados (md5), sin la marca de Gemini (recortar el 3,5 % de abajo a la derecha), **originales a 2.400 px como máximo** y sin EXIF, texto alternativo que describe lo que se ve, sin velos. **Resolución mínima: 800 px de ancho para cualquier foto y 1.600 para una foto a sangre o de cabecera** (en Solvento se publicaron fotos de 360 y 530 px y una «borrosa, un horror»). Si una foto real no llega y no hay otra, se amplía ×2 con cuidado o se cambia el hueco por una pieza sin foto del catálogo; nunca se deja borrosa ni vacía | Claude |

## Fase 05 · Identidad

| Nº | Paso | Quién |
|---|---|---|
| 19 | **Kit de marca y uso gráfico.** Todas las versiones del mismo dibujo; **la versión clara del logo para fondos oscuros**. Si el logotipo es bueno, se usa como recurso gráfico (objeto 3D, pie, marcas de agua). **El símbolo se nombra por lo que es** | Jean Paul |

---

## Fase 06 · Firma gráfica (día 2)

| Nº | Paso | Quién |
|---|---|---|
| 20 | ✋ **Plantilla y nivel de movimiento.** (a) **Una pregunta a Álvaro: ¿qué nivel de movimiento quiere?** — *quieto*, *medio* o *«como GYF»* (tabla de abajo). Si no contesta, se elige el que pida el sector de la competencia más fuerte y se apunta. (b) **Plantilla nueva, siempre:** Jack propone **tres nuevas** que den ese nivel (B1-B10), elige Álvaro y Jack la destripa. Si el cliente trae una referencia, esa manda. (c) La biblioteca **no** se usa aquí para elegir base: entra en el 21 (catálogo) y, si el resultado cojea, como recurso (regla de plantilla del paso cero B). **Se puede adelantar al día 0** si hay referencia o prisa; entonces el tema en código (B10) es condición del paso 23, no del 20 | Jack · Álvaro |
| 21 | **Ficha de firma gráfica** (`07-FIRMA-GRAFICA/FIRMA.md`) **desde el catálogo de piezas**: zona por zona (portada, al bajar, servicios, fotos, sección propia, cifras, banda, pie, cabecera, conversión, lectura), **qué pieza va y de dónde sale**, con el **mínimo del nivel pedido**. Se cambian las seis piezas que obliga `VARIACIONES.md` y se respeta lo marcado «No repetir». **Al menos una pieza nueva o adaptada al motivo del cliente** (en Solvento: el paso a paso del amianto). Con qué se sustituye cada visual (mismo peso). **Alto del logo en la cabecera medido contra la demo.** Lleva también la **tabla de llamadas a la acción**, página a página: pregunta del lector → titular → botón principal y secundario (principio 9), que se vuelca en `PIE_FRASES` y en los botones. Cualquier estilo nuevo se prueba con 3 piezas. **Maqueta con TODAS las secciones, comparada lado a lado con la demo y con la web de GYF** (es la vara de medir de «gracia» que usa Álvaro) | Jean Paul · Dani · Kubrick |
| 22 | ✋ **Álvaro da el visto bueno a la dirección visual** con la maqueta delante. Tres estados en la ficha: **aprobado por Álvaro**, **decidido por Jean Paul (revisable)** y **aprobado por delegación** (Álvaro dice «que decida Jean Paul»). Antes de enseñarla, **detector, filas de diseño** | Álvaro (o Jean Paul por delegación) |

**Niveles de movimiento** (el mínimo que exige la ficha de firma; se puede poner más):

| Nivel | Qué lleva como mínimo |
|---|---|
| **Quieto** | Aparición al entrar (R18), botones que ruedan, cabecera, opiniones y FAQ. Nada clavado ni con scrub |
| **Medio** | Lo de «quieto» + paralaje de fotos (E1), una cinta (C5), cifras que cuentan (G3), texto que se enciende en ordenador (C1) y una transición fuerte al final (I1 o I2) |
| **«Como GYF»** | Lo de «medio» + **una portada con golpe** (A1-A4 u objeto 3D H1), **una pieza clavada o de scroll propia** (F1, F2, D6), **una pieza de marca en el pie** (J3, J4, H2), **un cambio de tono fuerte entre secciones** (B1 o F3) y una pieza nueva o adaptada al motivo del cliente |

**Lo que puede repetirse de una web a otra** es lo que es función (tarjeta de llamada, estado
abierto o cerrado, nota de Google, opiniones, cabecera fija); su aspecto cambia.

## Fase 07 · Construir

| Nº | Paso | Quién |
|---|---|---|
| 23 | Crear el repositorio del cliente **copiando entero el `tema/` de la plantilla** (o el repositorio de la última web que la usó, si tiene piezas mejores) y rellenando `config.py`, `tema.css`, `recursos/` y `contenido/`. **Las piezas del catálogo que estén en otro repositorio se copian de allí** (la columna «Código» dice dónde). Álvaro crea el repositorio de GitHub y el proyecto de Vercel con la lista de alta (Root Directory `sitio`) | Claude · Álvaro |
| 24 | Configurar: datos del negocio desde la ficha, `resenas.json`, GTM, casos, logotipos, `PIE_FRASES` de la tabla de llamadas a la acción, la firma de GYF y las piezas del motivo del cliente | Claude |
| 25 | **Generar**: `build.py` → `rematar.py` → `controles.py`. La capa de movimiento según el nivel del paso 20. Nunca se toca `sitio/` a mano | Claude · Kubrick |
| 26 | Comprobar que el SEO técnico ha salido completo | Claude |
| 27 | **Entregar** con `entrega.py` (tandas < 100 archivos y < 25 MB, `repositorio-vN`, `LEEME.txt`) y **una imagen de resumen** | Claude |

## Fase 08 · Controlar a máquina y con el detector

| Nº | Control | Qué comprueba | Quién |
|---|---|---|---|
| 28 | `controles.py` | Lo de siempre (H1, title, meta, canónicas, enlaces, contrato, sitemap, restos de markdown, notas de maqueta, subtítulos vacíos, mayúsculas, horarios falsos, fotos repetidas en la página, tablas o citas sin convertir, declaraciones largas, fotos pendientes) **y desde la v11**: **ERROR** si una foto tiene menos de 800 px de ancho o una foto a sangre menos de 1.600 · **ERROR** si aparece una frase de la columna «no se dice nunca» de `PROMESAS.md` · **AVISO** si una página no tiene «Lector:» y «Decide:» · **AVISO** si una página usa el pie de defecto o comparte frase de pie con otra · **AVISO** si el botón principal del pie no es el de la tabla de llamadas a la acción · **AVISO** si un dato del inventario del paso 2 no aparece en ninguna página. Cero errores y cero avisos | Claude |
| 29 | `control29.py` | Capturas a **390, 768, 1.024, 1.280 y 1.440**; desborde; contraste del texto sobre foto; cookies que no tapan el botón; formularios; texto invisible; menú; consola sin errores; primera pantalla del móvil | Claude |
| 30 | Lighthouse móvil | **Tras cada vuelta de diseño**, mediana de 5 pasadas. Home ≥ 85, landings ≥ 95, accesibilidad ≥ 95, SEO 100. Si baja, A/B contra la versión anterior | Claude |
| 31 | Vista previa publicada | Lo que se revisa es lo que sirve Vercel, con `?v=N` | Claude · Álvaro |
| 31b | **El detector** | Se pasa **la tabla entera de «El detector»** sobre la web generada, fila a fila, con capturas delante. Cada fila que salta lleva a su paso y se arregla en **toda** la web antes de enseñarla a nadie. Emil revisa hover, transiciones y curvas. El resultado va a `ESTADO.md` | Claude · Emil |

**Regla:** un control que salta no se silencia. Se cambia el diseño o el texto, no el control
(salvo un falso positivo demostrado, que se documenta en el propio control).

## Fase 09 · Prueba con personas

| Nº | Paso | Quién |
|---|---|---|
| 32 | **Dos personas ajenas como mínimo** miran la web **en su móvil**, sin explicación: *¿qué es lo primero que ves?* y *¿qué harías ahora?* **Si se puede, una del perfil del lector principal** (en Solvento, un administrador de fincas) | Álvaro |
| 33 | ✋ **Álvaro da por buena la web** y se la pasa al cliente. Lo que corrija se busca primero en el detector | Álvaro |

## Fase 10 · Auditar

| Nº | Paso | Quién |
|---|---|---|
| 34 | **Briefing** con la lista de URLs **generada desde el sitemap**, el lector principal, `PROMESAS.md` y el aviso del `noindex`. **Seis agentes invocados de verdad**, en tandas de dos o tres, sin verse; cada informe a `09-AUDITORIA` en cuanto llega y al registro de agentes. Formato idéntico, con nota y «lo que no he podido verificar». **[E]** También puntúan la web vieja | Matías · Bruno · Dani · Jean Paul · Merche · Turing |
| 35 | **Contrastar con el código, después y nunca antes.** Un solo documento: alta, media y baja, descartados y ⚑ | Claude |
| 36 | **Arreglar todo lo que no depende de una decisión.** Las ⚑, en una sola tanda | Claude |
| 37 | **Reauditar** con los mismos seis y **5 aspectos fijos por disciplina** | Los seis |
| 37b | **Objetivo: 9 o más en las seis disciplinas.** Turing, en dos notas: «en la web» y «fuera de la web» | Los seis · Claude |
| 37c | **Cierre de pendientes:** PDF con la marca GYF en tres bloques, con casillas; lo del cliente, en un WhatsApp de tres o cuatro preguntas | Claude |

## ¿Está terminada?

**Una web está terminada, lista para publicar, cuando están cerrados los pasos 1-37**: subida a
GitHub, bien en la vista previa, **detector pasado**, prueba con personas hecha, cero ⚑, **registro de
agentes completo** y la auditoría a 9. Cuando Álvaro pregunta «¿lo damos por terminado?», la respuesta
es **sí o no y por qué**, y después lo que queda en tres grupos.

## Fase 11 · Publicar

| Nº | Paso | Quién |
|---|---|---|
| 38 | ✋ **Álvaro da la orden de publicar** | Álvaro |
| 39 | **[E]** Copia de seguridad doble de la web vieja | Claude · Álvaro |
| 40 | Paquete de producción desde el último commit aprobado. **[E]** Vaciar **solo** la carpeta del dominio y subir | Claude |
| 41 | Comprobar el `.htaccess` y que **producción no lleva el `noindex`** | Bruno |
| 42 | **Verificar en producción**: home, servicio, landing, 404, sitemap, robots, www y https, **y una muestra de las 301** | Claude |

## Fase 12 · Después de publicar

| Nº | Paso | Quién |
|---|---|---|
| 43 | Retirar o proteger la vista previa de Vercel | Álvaro |
| 44 | **Probar el formulario de verdad** (con adjunto, si lo lleva) | Claude · Álvaro |
| 45 | Medición con consentimiento; conversiones de Ads | Claude |
| 46 | **Search Console** y ficha con la web enlazada | Claude · Álvaro |
| 47 | NAP igual en todas partes. **[E]** Borrar el WordPress viejo tras una semana sin incidencias | Matías · Turing |
| 48 | **Medir y cerrar**: a las 2, 6 y 12 semanas. **Actualizar el sistema**: protocolo (versión siguiente desde `CAMBIOS-PARA-PROTOCOLO-v<N+1>.md`), **filas nuevas del detector**, **piezas nuevas al catálogo con su captura**, tema a la biblioteca, registro de uso, skills (Demiurgo) y archivos de arranque | Iñaki · Demiurgo · Claude |

---

# EL DETECTOR: CUANDO UNA WEB COJEA

Se pasa entero en el **paso 31b**; las filas de contenido, en el **15**, y las de diseño, en el **22**.
Y **siempre que Álvaro se queje de algo**: se busca su síntoma aquí antes de tocar nada. Cada fila dice
cómo se ve, qué paso falló y qué se hace. Si un síntoma no está, se añade a `CAMBIOS-…` el mismo día.

### Contenido

| Síntoma («cojea porque…») | Cómo se ve | Paso que lo arregla | Qué se hace |
|---|---|---|---|
| **Hay poca información; el contenido es pobre** | El lector no sabe si es obligatorio, cuánto tarda, quién paga, qué pasa en su casa; datos del inventario sin usar | 2 · 15d | Lista de huecos por página (Merche y Dani) y el inventario de datos usado entero; lo que decide va en la página del servicio |
| **Habla de quien no nos importa** | Particulares en el menú y en los textos de una web para administradores | 2 · 11 | Lector principal fijado; los secundarios, fuera del menú y al pie |
| **Promete lo que no hacemos** | «Presupuesto con una foto», «atención rápida» con «no hacemos urgencias» | 2b · 13 · 28 | Frase sustituida por la de `PROMESAS.md` en **toda** la web; el control la caza |
| **Lo importante está escondido** | Lo legal o lo económico, en preguntas frecuentes y no en el servicio | 13 · 15d | Se sube a la página del servicio con su H2 en pregunta |
| **El tono no es del lector** | Tutea a un profesional, o le explica lo que ya sabe | 2 · 13 | Voz del paso 2 y criterio de Merche |

### Llamadas a la acción

| Síntoma | Cómo se ve | Paso | Qué se hace |
|---|---|---|---|
| **El botón no responde a la frase** | «¿Busca una empresa solvente?» → «Mándenos una foto» | 21 · 24 | Tabla de llamadas a la acción: pregunta → respuesta → acción |
| **La misma llamada o el mismo pie en todas las páginas** | Una frase de pie para trece páginas | 13 · 24 · 28 | `PIE_FRASES` por URL; el control avisa |
| **La frase grande no es certera** | Titular genérico («Contacte con nosotros») | 13 · 21 | El titular responde a la pregunta del antetítulo en cinco palabras o menos |

### Diseño y movimiento

| Síntoma | Cómo se ve | Paso | Qué se hace |
|---|---|---|---|
| **Está sosa; «la puede hacer un niño de 10 años»** | Comparada con la web de GYF o con la demo, le faltan golpe, capas y movimiento | 20 · 21 | Preguntar el nivel; ficha con el mínimo del nivel; maqueta comparada lado a lado; si la plantilla nueva no da más, piezas del catálogo o base de la biblioteca |
| **La plantilla no da lo que se pide** | El nivel pedido es «como GYF» y la plantilla nueva es sobria | 20 · 21 | Se ve en la maqueta del 21: se tira del catálogo y, si no basta, de una plantilla de la biblioteca con tema en código, antes de construir y no después |
| **Hueco o caja vacía al quitar algo** | Una foto rechazada deja una columna en blanco | 21 (principio 6) | Se sustituye con el mismo peso: otra foto, objeto o pieza del catálogo |
| **El logo es pequeño o no se ve** | Logo de 28 px en una cabecera de 90; logo oscuro sobre fondo oscuro | 19 · 21 | Alto medido contra la demo; versión clara en cabeceras oscuras |
| **La cabecera desaparece al bajar y no se ve el menú** | Al hacer scroll se va el logo, el teléfono y el menú | Base (cabecera) · 29 | Cabecera siempre a la vista; el tema de la plantilla no puede esconderla (el `main.js` de 003 lo hacía) |
| **En el móvil la página es más ancha que la pantalla** | El menú o el botón quedan fuera; el navegador aleja la página | 29 | Ninguna pista horizontal (pasos, galería, cinta) ensancha la página: `contain:paint` o `overflow` en su contenedor; `control29.py` mide `innerWidth` = 390 |
| **Todo es igual de importante** | Sin cambio de tono entre secciones, todas blancas | 21 | Una pieza de cambio de tono (B1, F3, I4) |

### Fotos

| Síntoma | Cómo se ve | Paso | Qué se hace |
|---|---|---|---|
| **Foto borrosa** | Foto de menos de 800 px estirada; cabecera a sangre de 1.000 | 18 · 28 | Otra foto, ampliación ×2 o pieza sin foto; el control da error |
| **Foto vieja o que no es moderna** | Un taller antiguo, una lona con un teléfono viejo | 16 · 18 | Foto real reciente del cliente (en Solvento, la furgoneta rotulada) o Gemini con decisión de Álvaro |
| **Foto repetida en la misma página** | La misma bajante en galería, pasos y texto | 16 · 28 | Listas de fotos por pieza que cogen la primera no usada en la página |

### Proceso

| Síntoma | Cómo se ve | Paso | Qué se hace |
|---|---|---|---|
| **No se sabe qué agentes han trabajado** | Documentos firmados por agentes sin informe | Cómo se usa · 34 | Registro de agentes; se invoca o se dice «sin agente» |
| **El cliente está cansado de preguntas** | Tres rondas, datos que ya teníamos | 4 | Buscar antes; una tanda y una de aclaraciones |
| **Se trabajó sin el protocolo** | Estrategia o plantilla hechas antes de subir los archivos del sistema | 1 | Comprobación del sistema antes de nada |
| **No se ve en Vercel (404)** | Despliegue correcto y página en blanco o 404 | Stack | Root Directory = `sitio` |
| **GitHub rechaza la subida** | Más de 100 archivos o más de 25 MB | 27 | `entrega.py` con límites |
| **Veinte retoques sueltos** | Álvaro corrige lo mismo en varias páginas, una a una | Este detector | Volver al paso de la fila y aplicarlo a toda la web; si no hay fila, `CAMBIOS-…` |

---

# LAS REGLAS QUE NO SE NEGOCIAN

1. **La web vieja no se toca** hasta el día del cambio [E].
2. **Mismo objetivo: URLs idénticas. Objetivo nuevo: URLs nuevas con 301 de un solo salto** [E].
3. **Los legales se corrigen, no se reescriben.**
4. **Manda la ficha de Google.** No se añade ningún dato que la ficha no tenga.
5. **Nada inventado**: reseñas, cifras y citas reales; datos de municipio con fuente oficial.
6. **Plantilla: primero, siempre, una nueva con Jack; la biblioteca, solo si el resultado no funciona.** Se toman
   comportamientos y números, nunca su código. No se compra. Se elige por calidad, jamás por sector.
7. **La plantilla se traslada y no se adelgaza**: lo que se quita se sustituye con el mismo peso.
8. **La conversión se decide en la ficha de firma**, antes de construir, con la tabla de llamadas.
9. **La vista previa nunca se indexa, y producción nunca lleva el `noindex`.**
10. **Solo se entregan los archivos que cambian**, en tandas que GitHub acepta (< 100 archivos,
    < 25 MB), y la copia completa se mantiene al día.
11. **Ninguna ⚑ llega a GitHub.** Antes de la primera subida, el contenido está cerrado.
12. **Tras un rechazo, se vuelve atrás y se hace un solo cambio.** Para deshacer, el commit anterior.
13. **Dato y estimación se separan siempre**; lo que no se ha comprobado se llama «no comprobado».
14. **Dos hipótesis fallidas seguidas: se deja de diagnosticar y se prueba por eliminación (A/B).**
15. **`ESTADO.md` en la carpeta y en el proyecto al cerrar cada paso.**
16. **El sistema y el cliente, en proyectos separados.** Ningún trabajo se da por cerrado sin decir
    qué no se sabe.
17. **Solo se promete lo que está en `PROMESAS.md`**, validada por Álvaro.
18. **Cada paso de agente lo hace el agente, invocado, y queda en el registro.** Si no, se dice.
19. **El botón responde a la pregunta.** Cada llamada a la acción sale de la tabla del paso 21.
20. **Lo que Álvaro corrige se arregla vía protocolo**: fila del detector, paso, toda la web. Lo que
    corrige dos veces es un fallo del protocolo y va a `CAMBIOS-…` ese día.

---

# TRAMPAS DOCUMENTADAS

| Qué pasó | Dónde | Cómo se evita |
|---|---|---|
| Lista de plantillas buscadas por el oficio del cliente | Marcos | B1: por calidad, nunca por sector |
| Estudio de la plantilla con tokens y poco más: la v1 salió plana | Balgas | B3-B10 completos |
| La portada partida en dos columnas | Balgas | B5 y paso 21 |
| En el móvil, lo primero era un párrafo | Balgas | Pasos 29 y 32 |
| Canónicas sin www con la web viva con www | Marcos | Paso 8 |
| Formulario que nunca había enviado un aviso | Marcos | Pasos 6 y 44 |
| Legales en blanco por el `IntersectionObserver` al 12 % | Marcos | Paso 29 |
| Web caída por bucle de redirecciones detrás del proxy | Marcos | `.htaccess` con `X-Forwarded-Proto` |
| Notas de maqueta publicadas, subtítulos vacíos, enlaces perdidos | Balgas | Pasos 13 y 28 |
| «Ver opiniones» abría Maps con la competencia | Balgas | Ficha por su CID |
| La home cayó de 88 a 63 tras añadir diseño | Balgas | Paso 30 tras cada vuelta |
| Respuestas del cliente llegadas con los textos hechos | Balgas, GYF | Paso 4, el día 0 |
| Fotos de Gemini asignadas por orden de llegada | Balgas | Paso 17: por contenido |
| Logo hecho con IA: cada versión era un dibujo distinto | Balgas | Paso 19 |
| URL falsa en el briefing de auditoría | Marcos | Paso 34: URLs desde el sitemap |
| Álvaro arrastró las carpetas `TANDA` en vez de lo que hay dentro | Balgas | `LEEME.txt` |
| La FAQ negaba algo que el cliente sí hace | Balgas | Pasos 4 y 13 |
| Tablas de Markdown publicadas en crudo | Balgas | Paso 28 |
| Texto a 1,9:1 sobre foto clara | Balgas, GYF | Paso 29 |
| El aviso de cookies tapaba el botón de llamar | Balgas | Paso 29 |
| Arquitectura hecha antes de ver Search Console | GYF | Pasos 8-9 antes del 11 |
| Nueve horas perdidas por una caída de la conexión | GYF | Regla 15 |
| Fotos de Gemini en lote que se contaminaban | GYF | Paso 17: una conversación por foto |
| Objetos 3D de Gemini como iconos: rechazados | GYF | Paso 21: prueba de 3 piezas |
| v1 «sosa y blanca»: se quitó lo que no gustaba sin sustituirlo | GYF | Principio 6 y maqueta comparada |
| El nombre de la persona y recuentos pequeños destacados | GYF | Principio 7 |
| «Profesionales de confianza» borró a las personas detrás de los agentes | GYF | Paso 13 |
| Un parque empresarial que era un estadio (Butarque) | GYF | Paso 15: fuente oficial |
| El logotipo en `<use>` no se veía | GYF | `viewBox` en `0 0 ancho alto` |
| Velo fucsia en `mix-blend-mode`: −3 puntos | GYF | Paso 18: sin velos |
| Tanda de 44 MB rechazada por GitHub | GYF | Paso 27 |
| La cabecera se escondía al bajar y con ella el menú | GYF | Base: cabecera siempre a la vista |
| Reseñas de largos muy distintos | GYF | Base: tarjetas iguales con «Leer más» |
| El repositorio se perdió al cerrar la conversación | GYF | Copia completa en cada versión |
| Pantallas de las maquetas borrosas | GYF | Paso 16: capturas HD y zoom 3 |
| 30 archivos «cambiados» que solo cambiaban de permisos | GYF | `core.fileMode false` |
| Google leía tres veces el texto de los botones | GYF | Base: texto una vez |
| Perfiles de Facebook con el nombre de la marca que eran de otros | GYF | Paso 5 |
| «Hasta el viernes no se puede» por el límite de uso | GYF | Se dice que es el límite de uso |
| La plantilla de Balgas se volvió a proponer para GYF sin cambiar sus piezas | GYF | Regla 6: si se repite, cambian las seis piezas de `VARIACIONES.md` |
| Una descarga guardada como «h.jpg» | GYF | Paso 18: se recoge cualquier nombre y se renombra |
| Falsos desbordes en el control por fotos recortadas | GYF | `control29.py` ignora lo que recorta un `overflow:hidden` |
| Aviso de cookies y fondo lateral de la web del cliente dentro de la maqueta | GYF | Paso 16: `RECORTE_HD` |
| Un archivo de 117 bytes al pasar el paquete a la carpeta | GYF | Envío por identificador y tamaño comprobado |
| Un caso presentado donde quiere posicionarse, no donde está el local (Dotti) | GYF | Base: municipio real y «El caso más cercano» |
| «Ver la web» en un caso que no tiene web | GYF | Base: «Ver la ficha» |
| Muestras de trabajos con un objeto genérico en vez de su web | GYF | Base: cada muestra con su maqueta |
| Traspaso pegado en el chat, cortado dos veces | Pousada | `TRASPASO.md` en el proyecto y en la carpeta |
| Foto de partida de Search Console perdida en el chat | Pousada | Paso 9: a `00-AUDITORIAS` en el momento |
| «Madrid no interesa» en un distribuidor de Madrid | Pousada | Paso 11: negocio de barrio o distribuidor |
| Prueba de arranque que no podía borrar su archivo | Pousada | Paso 1: permiso de borrado al empezar |
| Se trabajó un día sin los archivos del sistema en el proyecto | Solvento | Paso 1: comprobar el sistema antes de nada |
| Copia del LEEME de la biblioteca desfasada | Solvento | Paso 1 y 48: se sube el `LEEME.md` de la biblioteca |
| Tres rondas de preguntas; un dato que ya tenía Álvaro | Solvento | Paso 4 |
| Un Excel que el cliente no podía abrir en su iPad | Solvento | Paso 4: preguntar con qué abre |
| Solo 9 de 61 reseñas en Maps | Solvento | Paso 3: vista del propietario |
| Cuatro agentes a la vez agotaron el límite semanal | Solvento | Tandas de dos o tres; informe a la carpeta al llegar |
| Chrome solo dejaba bajar la primera foto de Gemini | Solvento | Paso 17: Álvaro baja todas desde la Biblioteca |
| Crafto, ya en la biblioteca, entró entre las tres y salió elegida | Solvento | B1.5: siempre tres nuevas |
| El filtro de 20 votos solo dejaba plantillas de 2015 | Solvento | B1: filtro para plantillas recientes |
| **v1 con todos los controles en verde y contenido pobre para el administrador** | Solvento | Principio 8 y paso 15d |
| **Particulares en el menú de una web para administradores** | Solvento | Pasos 2 y 11 |
| **«Presupuesto con una foto» publicado en toda la web** | Solvento | Paso 2b, `PROMESAS.md` y control 28 |
| **«Atención rápida» con «no hacemos urgencias»** | Solvento | Paso 2b |
| **Archidex por sobria: «sosa», «la puede hacer un niño de 10 años»** | Solvento | Paso 20: nivel de movimiento; catálogo en el 21 |
| **El mismo pie en todas las páginas y «Mándenos una foto» a un administrador** | Solvento | Principio 9, tabla de llamadas y `PIE_FRASES` |
| **Fotos de 360 y 530 px publicadas; una «borrosa, un horror»** | Solvento | Paso 18 y error en el control 28 |
| **Al cambiar una foto, la caja de al lado se quedó vacía** | Solvento | Principio 6 |
| **Logo pequeño en la cabecera** | Solvento | Paso 21: alto medido contra la demo |
| **Ficha de firma «de Jean Paul» sin haberlo invocado** | Solvento | Registro de agentes y regla 18 |
| **Vercel en 404 por la carpeta raíz** | Solvento | Stack: Root Directory `sitio` |
| **Texto que se enciende con contraste bajo en el móvil** | Solvento | Base: sin scrub de texto en táctil |
| **La cabecera se escondía al bajar: el tema de Rayo traía la variación que la esconde** | Solvento | Base: siempre a la vista; corregido también en `003-RAYO/tema` |
| **La pista de pasos ensanchaba la página en el móvil a 1.560 px y el menú quedaba fuera** | Solvento | Detector y control 29 (`innerWidth`) |

---

# CÓMO SE ARRANCA UN CLIENTE

Con los **cuatro archivos del sistema en los archivos del proyecto**: `01-PROTOCOLO-WEB.md` (este
protocolo), `02-EMPIEZA-AQUI.md`, `03-BIBLIOTECA-LEEME.md` (copia del `LEEME.md` de la biblioteca) y
`04-BIBLIOTECA-REGISTRO-DE-USO.md`, junto a lo del cliente. Álvaro crea el proyecto, sube esos archivos,
conecta la carpeta del cliente y la de la biblioteca (`000-BIBLIOTECA PLANTILLAS`), abre un chat y pega
**`PROMPT-ARRANQUE.md`** con los corchetes rellenos. Las fichas, variaciones, capturas, temas y el
**catálogo de piezas** se leen de la carpeta de la biblioteca, no se suben al proyecto.

Lo primero que devuelve Claude es un **resumen de una página** del cliente (qué hace, qué no, **a quién
se dirige la web y qué tiene que decidir**, qué dudas quedan), **el borrador de `PROMESAS.md`** para que
Álvaro lo valide y, en el mismo mensaje, **la tanda del paso 4**.

---

# LO QUE TODAVÍA NO SE SABE

- **Los plazos no están cronometrados.** La próxima web apunta en `ESTADO.md` la hora de inicio y
  fin de cada fase.
- **El caso N no se ha probado** con este protocolo.
- **El detector y el catálogo son de la v11 y no se han pasado aún en una web desde el principio.** Se
  escribieron con lo que falló en Solvento; la próxima web dirá qué filas sobran o faltan.
- **Los controles nuevos del paso 28 no están todos en código.** Hoy solo da error la foto de menos de
  800 px (en el repositorio de Solvento v2). Promesas, «Lector:» y «Decide:», pie por página, fotos a
  sangre e inventario de datos se escriben en `003-RAYO/tema/generador/controles.py` antes de la
  próxima web; hasta entonces, Claude los comprueba a mano en el 31b y lo dice.
- **Los niveles de movimiento** se han definido con tres webs (Balgas, GYF y Solvento v2).
- **La auditoría a ≥ 9 se ha medido en local** (Balgas y GYF). **Solvento v2 no se ha auditado** con los
  seis agentes.
- **Lighthouse en Vercel**: sin cifra en ninguna web. Solvento v2 en local (móvil): rendimiento 86-99 y
  100 en lo demás.
- **Safari, móvil real y el 3D con tarjeta gráfica real**: sin comprobar en Solvento v2.
- **La descarga de Gemini** por la Biblioteca: probada una vez.

---

*v11 (03/10/2026, Solvento v2 y Pousada): el detector (síntoma → paso → qué se hace), pasado en el 15,
el 22 y el 31b y siempre que Álvaro corrige; el catálogo de piezas de toda la biblioteca, usado en el 21
y alimentado en el 48 (B11); principios 8 (lector y decisión) y 9 (el botón responde a la pregunta);
lista de promesas validada por Álvaro (2b) y control de promesas; lector principal e inventario de
datos (2); juicio del contenido contra el objetivo con Merche y Dani (15d); nivel de movimiento
preguntado y plantilla nueva siempre, con la biblioteca como recurso si el resultado no funciona (20 y paso cero B); ficha de firma desde el catálogo con mínimos por nivel, tabla de
llamadas a la acción, alto del logo y tres estados de aprobación (21-22); cada paso con su agente
invocado y registro de agentes (regla 18); fotos ≥ 800 px y ≥ 1.600 a sangre con error en el control;
pie por página (`PIE_FRASES`) en la base; Vercel con Root Directory `sitio`; tandas con límites en
`entrega.py`; reseñas desde la vista del propietario; preguntas al cliente acotadas; diagnóstico en
tandas; Gemini bajado por Álvaro desde la Biblioteca; traspaso y foto de partida guardados en el
momento; distribuidores en el paso 11; filtro B1 para plantillas recientes; B10 permitido en el
cliente; veintisiete trampas nuevas.*

*v10 (27/09/2026 noche, cierre de la web de GYF en la v5.7): traspaso entre conversaciones; límite de
uso dicho como tal; `_to_delete/` vaciado con permiso; entrega por contenido; capturas HD y maquetas;
opiniones por página; cabecera siempre a la vista; prueba con dos personas; nota de Turing en dos;
qué es «terminada»; doce trampas nuevas.*

*v9 (27/09/2026, web de GYF): una plantilla nueva por web; caso E con objetivo nuevo; pasos 8-9 antes
del 11; perfiles externos; cero ⚑ antes de GitHub; fotos artísticas de Gemini; el logotipo como
recurso gráfico; la plantilla no se adelgaza; maqueta comparada; principio 7; dieciséis trampas.*

*v8 (26/09/2026): lista fija de preguntas el día 0; H1 sin canibalizar; formularios sin casilla;
cierre de pendientes. v7: objetivo de 9 en las seis disciplinas. v6: el equipo de agentes, un solo
protocolo E/N, 48 pasos. v5: GitHub → Vercel → hosting. v4: método ThemeForest. v1-v3: Marcos.*

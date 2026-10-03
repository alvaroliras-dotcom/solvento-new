# Solvento · web v2 (tema 003 GYF-Rayo)

Web estática de solvento.es, hecha el 03/10/2026 sobre el tema **003-RAYO** de la biblioteca GYF (el de la web de
El Gordo y el Flaco) con la firma propia de Solvento. Sustituye a la v1 (tema 007-Archidex).

## Generar

```
python3 generador/build.py && python3 generador/rematar.py && python3 generador/controles.py
python3 -m http.server 8765 --directory sitio
```

`sitio/` es lo que se publica (en Vercel: Root Directory = `sitio`). No se toca a mano.

## Qué se toca

| Archivo | Qué |
|---|---|
| `contenido/paginas/*.md` | Los textos (paso 27). Marcadores: `(FOTO: descripción — archivo.jpg)`, `(Bloque de opiniones… n.º X… Fragmento literal: «…»)` |
| `contenido/resenas.json` | Nota, número de reseñas, las 8 opiniones del carrusel (`opiniones`) y las 61 literales (`todas`) |
| `generador/config.py` | Datos, menú, servicios, galería, cifras, pasos del amianto, textos y frases del pie |
| `cliente/css/tema.css` | Colores, fuente y las piezas propias de Solvento (portada verde noche, amianto paso a paso, pie) |
| `generador/mapa301.json` | Redirecciones 301 y 410 de la web antigua (Bruno) |
| `recursos/` | Fotos, marca, la gota en 3D (`objeto/gota-3d.png`, la genera `herramientas/objeto3d/foto_fija.py`) |

## Piezas de la firma de Solvento

- Portada verde noche: H1 grande con la zona en turquesa, la gota del logo en 3D (three.js diferido; la imagen fija es
  el LCP) y tres sellos. La galería de fotos sube por encima de la portada fija.
- Hoja clara que sube con la cinta gigante de servicios.
- Servicios en filas con la foto que sigue al ratón.
- **El amianto, paso a paso**: sección clavada que avanza de lado con el scroll (en la portada, en la del amianto, en
  la de administradores y en las de municipio).
- Cifras en mosaico (20 administradores, 90 %, 10.000 € de cabina, 1,3 M€), opiniones en carrusel, FAQ.
- Interiores: foto de cabecera a sangre con paralaje, columna de lectura con índice, citas de opiniones.
- Presupuesto por foto (hasta 3 fotos, `enviar.php` con adjuntos) y «Le llamamos».
- Pie verde noche con la frase de cada página y la gota grande.

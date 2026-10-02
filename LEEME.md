# solvento.es · web nueva (2026)

Generada con el tema **GYF-Archidex** (biblioteca `007-ARCHIDEX`) y la firma de `07-FIRMA-GRAFICA/FIRMA.md`.

- Generar: `bash herramientas/servir.sh` (build → rematar → controles → http://localhost:8765). Nunca se toca `sitio/` a mano.
- Vercel: raíz del proyecto = `sitio`. La vista previa lleva `X-Robots-Tag: noindex` (`sitio/vercel.json`).
- Hosting del cliente (Apache, acepta `.htaccess`): se sube el contenido de `sitio/`. El `.htaccess` lleva sin www y https en un salto, las 53 redirecciones 301 y los 201 410 del mapa de Nuria, y las reglas por patrón.
- Formularios: `sitio/enviar.php` (presupuesto por foto y candidatura, con adjuntos) a info@solvento.es.
- Datos del cliente: `generador/config.py`. Textos: `contenido/paginas/`. Reseñas literales: `contenido/resenas.json`. Fotos: `recursos/fotos/` (texto alternativo en `generador/alt_fotos.json`).

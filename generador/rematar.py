# -*- coding: utf-8 -*-
"""GYF-Rayo · Rematar (paso 52): siempre el ÚLTIMO del build.
Copia recursos, genera imágenes 800/1600 en JPG y WebP, une y minifica el CSS,
y deja los archivos de servidor (.htaccess, enviar.php, favicons, manifest)."""
import os, re, shutil, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import (VERSION, NEGOCIO as N, DOMINIO, MARCA, COOKIES_CLAVE, HOST_PRODUCCION, COLOR_TEMA, REDIRECCIONES,
                    REDIRECCIONES_302, URLS, OBJETO_PORTADA, texto, FOTO_MAX_MB)
import json

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = lambda *p: os.path.join(RAIZ, *p)
S = lambda *p: os.path.join(RAIZ, "sitio", *p)


def css():
    base = open(R("base", "css", "base.css"), encoding="utf-8").read()
    tema = open(R("cliente", "css", "tema.css"), encoding="utf-8").read()
    # el tema va DESPUÉS de la base para que sus variables manden; las @font-face, arriba
    fuentes = "".join(re.findall(r"@font-face\{[^}]+\}", tema))
    tema = re.sub(r"@font-face\{[^}]+\}", "", tema)
    todo = fuentes + base + tema
    todo = re.sub(r"/\*.*?\*/", "", todo, flags=re.S)
    todo = re.sub(r"\s+", " ", todo)
    todo = re.sub(r"\s*([{}:;,>])\s*", r"\1", todo)
    todo = todo.replace(";}", "}")
    # restaurar espacios necesarios en selectores/valores que la regla anterior pudo tocar
    todo = re.sub(r"@media\(", "@media (", todo)
    todo = todo.replace(")and(", ") and (").replace("and(", "and (")
    os.makedirs(S("css"), exist_ok=True)
    open(S("css", "estilo.css"), "w", encoding="utf-8").write(todo)
    return len(todo)


def imagenes():
    """Fotos y casos (JPG/PNG/WebP) → 800 y 1600 en JPG y WebP. El objeto de portada (con alfa) → 420 y 840
    en WebP con alfa y 840 en PNG (respaldo)."""
    os.makedirs(S("img"), exist_ok=True)
    n = 0
    for carpeta in ("fotos", "casos"):
        d = R("recursos", carpeta)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                continue
            im = Image.open(os.path.join(d, f)).convert("RGB")
            b = f.rsplit(".", 1)[0]
            for w in (800, 1600):
                v = im if im.width == w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
                v.save(S("img", f"{b}-{w}.jpg"), "JPEG", quality=80 if w == 1600 else 78, optimize=True, progressive=True)
                v.save(S("img", f"{b}-{w}.webp"), "WEBP", quality=76, method=6)
            n += 1
    o = R("recursos", "objeto", OBJETO_PORTADA["imagen"])
    if os.path.exists(o):
        im = Image.open(o).convert("RGBA")
        b = OBJETO_PORTADA["imagen"].rsplit(".", 1)[0]
        for w in (420, 840):
            v = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
            v.save(S("img", f"{b}-{w}.webp"), "WEBP", quality=82, method=6)
        im.resize((840, round(im.height * 840 / im.width)), Image.LANCZOS).save(S("img", f"{b}-840.png"), "PNG", optimize=True)
    else:
        sys.exit(f"rematar: falta el objeto de portada recursos/objeto/{OBJETO_PORTADA['imagen']} (herramientas/objeto3d/foto_fija.py lo genera)")
    for k in ("video_webm", "video_mov"):
        if OBJETO_PORTADA.get(k):
            os.makedirs(S("objeto"), exist_ok=True)
            shutil.copy(R("recursos", "objeto", OBJETO_PORTADA[k]), S("objeto", OBJETO_PORTADA[k]))
    return n


def copiar():
    shutil.copytree(R("recursos", "fuentes"), S("fuentes"), dirs_exist_ok=True)
    for f in os.listdir(S("fuentes")):
        m = re.match(r"(.+)-latin-(\d+)-normal\.woff2", f)
        if m:
            os.replace(S("fuentes", f), S("fuentes", f"{m.group(1)}-{m.group(2)}.woff2"))
    os.makedirs(S("marca"), exist_ok=True)
    for f in os.listdir(R("recursos", "marca")):
        if f.endswith(".svg"):
            shutil.copy(R("recursos", "marca", f), S("marca", f))
    shutil.copy(R("recursos", "marca", MARCA["og"]), S("og-image.jpg"))
    for f in os.listdir(R("recursos", "favicon")):
        shutil.copy(R("recursos", "favicon", f), S(f))
    # el manifest sale de config.py (nombre y color), no se copia a mano
    open(S("site.webmanifest"), "w", encoding="utf-8").write(json.dumps({
        "name": N["nombre"], "short_name": N["nombre"][:12],
        "icons": [{"src": "/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png"}],
        "theme_color": COLOR_TEMA, "background_color": COLOR_TEMA, "display": "standalone"}, ensure_ascii=False))
    os.makedirs(S("js"), exist_ok=True)
    js()
    shutil.copytree(R("cliente", "js", "vendor"), S("js", "vendor"), dirs_exist_ok=True)
    shutil.copy(R("contenido", "resenas.json"), S("resenas.json"))


HTACCESS = r"""# __NOMBRE__ · servidor Apache (hosting Plesk del cliente)
Options -Indexes
DirectoryIndex index.html
AddType font/woff2 .woff2
AddType application/manifest+json .webmanifest
AddCharset utf-8 .txt

# Nada de copias, volcados ni registros a la vista
<FilesMatch "\.(zip|sql|bak|old|log|sh|ini|env|git.*|md|py|csv)$">
  Require all denied
</FilesMatch>
ErrorDocument 404 /404.html

<IfModule mod_rewrite.c>
RewriteEngine On
# Sin www (paso 18)
RewriteCond %{HTTP_HOST} ^www\. [NC]
RewriteRule ^ __DOMINIO__%{REQUEST_URI} [L,R=301]
# A https. Solo si ni Apache ni el proxy de Plesk (nginx delante) dicen que ya es https:
# así no entra en bucle detrás de un proxy (lo que tiró la web de Marcos).
RewriteCond %{HTTPS} off
RewriteCond %{HTTP:X-Forwarded-Proto} !https [NC]
RewriteCond %{HTTP:X-Forwarded-SSL} !on [NC]
RewriteRule ^ __DOMINIO__%{REQUEST_URI} [L,R=301]
# Restos del WordPress antiguo: 410 (ya no existen y no vuelven)
RewriteRule ^(wp-admin|wp-content|wp-includes|wp-json)(/.*)?$ - [G,L]
RewriteRule ^(wp-login\.php|xmlrpc\.php|wp-cron\.php|feed/?|comments/feed/?)$ - [G,L]
RewriteRule ^(author|category|tag|page)(/.*)?$ - [G,L]
# Sitemaps viejos de WordPress / Yoast / Rank Math → el nuevo
RewriteRule ^(sitemap_index\.xml|wp-sitemap\.xml|[a-z0-9_-]+-sitemap[0-9]*\.xml)$ /sitemap.xml [L,R=301]
# Redirecciones del cambio (paso 17)
__REDIRECCIONES__
# Temporales (302): URLs reservadas que volverán a servir 200
__REDIRECCIONES_302__
# Barra final en las URLs de carpeta
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_URI} !(\.[a-z0-9]{2,5})$ [NC]
RewriteCond %{REQUEST_URI} !/$
RewriteRule ^(.*)$ /$1/ [L,R=301]
</IfModule>

<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml application/json text/xml application/xml
</IfModule>

<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/html "access plus 0 seconds"
ExpiresByType text/css "access plus 1 year"
ExpiresByType application/javascript "access plus 1 year"
ExpiresByType image/jpeg "access plus 1 year"
ExpiresByType image/webp "access plus 1 year"
ExpiresByType image/svg+xml "access plus 1 year"
ExpiresByType font/woff2 "access plus 1 year"
ExpiresByType image/png "access plus 1 year"
ExpiresByType image/x-icon "access plus 1 year"
ExpiresByType image/vnd.microsoft.icon "access plus 1 year"
ExpiresByType application/manifest+json "access plus 1 week"
ExpiresByType application/json "access plus 0 seconds"
ExpiresByType application/xml "access plus 1 hour"
ExpiresByType text/xml "access plus 1 hour"
</IfModule>

<IfModule mod_headers.c>
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set X-Frame-Options "SAMEORIGIN"
</IfModule>
"""

ENVIAR = r"""<?php
/* __NOMBRE__ · formularios de la web: presupuesto por foto (contacto) y candidatura (trabaja con nosotros).
   Antispam: trampa + tiempo en la página + sin enlaces en el mensaje. Sin captcha.
   Adjuntos: hasta 3 archivos de __MAX__ MB (fotos; en la candidatura, también PDF y Word), comprobados por su
   contenido (finfo), no por la extensión. «t» lo rellena main.js: milisegundos con la página abierta. */
header('X-Robots-Tag: noindex');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: __CONTACTO__'); exit; }
$c = function ($k, $max) { return trim(mb_substr(strip_tags($_POST[$k] ?? ''), 0, $max)); };
$tipo = in_array($_POST['tipo'] ?? '', ['empleo', 'llamada'], true) ? $_POST['tipo'] : 'presupuesto';
$pagina = $c('pagina', 120);
if (!preg_match('#^/[a-z0-9\-/]*$#', $pagina) || strpos($pagina, '//') !== false) { $pagina = '__CONTACTO__'; }
$nombre = $c('nombre', 80); $telefono = $c('telefono', 20); $correo = $c('correo', 120); $donde = $c('donde', 160);
$mensaje = $c('mensaje', 2000); $quien = $c('quien', 20); $comunidad = $c('comunidad', 120); $necesita = $c('necesita', 80);
$oficio = $c('oficio', 40); $anios = $c('anios', 20);
$trampa = $_POST['web'] ?? ''; $t = (int)($_POST['t'] ?? 0);
$motivo = '';
if ($trampa !== '') { $motivo = 'trampa'; }
elseif ($t < 3000 || $t > 86400000) { $motivo = 'tiempo'; }
elseif ($nombre === '' || !preg_match('/^[0-9 +()\-]{9,20}$/', $telefono)) { $motivo = 'datos'; }
elseif (preg_match_all('#https?://#i', $mensaje) > 0) { $motivo = 'enlaces'; }
elseif ($correo !== '' && !filter_var($correo, FILTER_VALIDATE_EMAIL)) { $motivo = 'correo'; }
// Adjuntos
$tipos_ok = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp', 'image/heic' => 'heic', 'image/heif' => 'heif'];
if ($tipo === 'empleo') { $tipos_ok += ['application/pdf' => 'pdf', 'application/msword' => 'doc', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' => 'docx']; }
$adj = [];
if ($motivo === '' && !empty($_FILES['foto']) && is_array($_FILES['foto']['name'])) {
  $fi = function_exists('finfo_open') ? finfo_open(FILEINFO_MIME_TYPE) : null;
  for ($i = 0; $i < count($_FILES['foto']['name']) && count($adj) < 3; $i++) {
    if ($_FILES['foto']['error'][$i] === UPLOAD_ERR_NO_FILE) continue;
    if ($_FILES['foto']['error'][$i] !== UPLOAD_ERR_OK || $_FILES['foto']['size'][$i] > __MAX__ * 1048576) { $motivo = 'archivo'; break; }
    $tmp = $_FILES['foto']['tmp_name'][$i];
    $mime = $fi ? finfo_file($fi, $tmp) : '';
    if (!isset($tipos_ok[$mime])) { $motivo = 'archivo'; break; }
    $adj[] = ['nombre' => 'adjunto-' . ($i + 1) . '.' . $tipos_ok[$mime], 'mime' => $mime, 'datos' => file_get_contents($tmp)];
  }
}
$vuelta = $tipo === 'empleo' ? '/trabaja-con-nosotros/' : ($tipo === 'llamada' ? $pagina : '__CONTACTO__');
$clave = $tipo === 'llamada' ? 'llamada' : 'enviado';
$ancla_ok = $tipo === 'llamada' ? '#te-llamamos' : '#form-ok'; $ancla_ko = $tipo === 'llamada' ? '#te-llamamos' : '#form-error';
if ($motivo !== '') { header('Location: ' . $vuelta . '?' . $clave . '=0&motivo=' . $motivo . $ancla_ko); exit; }
$para = '__EMAIL__';
if ($tipo === 'llamada') {
  $asunto = 'QUE ME LLAMEN · ' . $nombre . ' · ' . $telefono;
  $cuerpo = "Petición de llamada desde la web.\n\nNombre: $nombre\nTeléfono: $telefono\nPágina: __DOMINIO__$pagina\n";
} elseif ($tipo === 'empleo') {
  $asunto = 'CANDIDATURA · ' . $nombre . ' · ' . $oficio;
  $cuerpo = "Candidatura desde la web.\n\nNombre: $nombre\nTeléfono: $telefono\nOficio: $oficio\nAños de experiencia: $anios\nMunicipio: $donde\n\n$mensaje\n";
} else {
  $quien_t = $quien === 'particular' ? 'Particular' : 'Administrador o comunidad';
  $asunto = 'PRESUPUESTO · ' . $necesita . ' · ' . $nombre . ($comunidad ? ' (' . $comunidad . ')' : '');
  $cuerpo = "Petición de presupuesto desde la web.\n\nQuién: $quien_t\nNombre: $nombre\nTeléfono: $telefono\nCorreo: $correo\nAdministración o comunidad: $comunidad\nDirección o municipio: $donde\nQué necesita: $necesita\n\n$mensaje\n\nFotos adjuntas: " . count($adj) . "\nPágina: __DOMINIO__$pagina\n";
}
$asunto = '=?UTF-8?B?' . base64_encode($asunto) . '?=';
$sep = 'sep-' . bin2hex(random_bytes(8));
$cab = "From: Web __NOMBRE__ <web@__HOST_SIN_WWW__>\r\n" . ($correo !== '' ? "Reply-To: $correo\r\n" : '') . "MIME-Version: 1.0\r\nContent-Type: multipart/mixed; boundary=\"$sep\"\r\n";
$m = "--$sep\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n\r\n$cuerpo\r\n";
foreach ($adj as $a) {
  $m .= "--$sep\r\nContent-Type: {$a['mime']}; name=\"{$a['nombre']}\"\r\nContent-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"{$a['nombre']}\"\r\n\r\n" . chunk_split(base64_encode($a['datos'])) . "\r\n";
}
$m .= "--$sep--";
$enviado = @mail($para, $asunto, $m, $cab);
header('Location: ' . $vuelta . '?' . $clave . '=' . ($enviado ? '1' . $ancla_ok : '0&motivo=envio' . $ancla_ko));
"""


def servidor():
    host = DOMINIO.split("//")[1]
    mapa = json.load(open(R("generador", "mapa301.json"), encoding="utf-8"))
    red = "\n".join([f"RewriteRule ^{re.escape(a.strip('/'))}/?$ {b} [L,R=301]" for a, b in mapa["r301"] if a != "/"]
                    + [f"RewriteRule ^{re.escape(a.strip('/'))}/?$ - [G,L]" for a in mapa["r410"]]
                    + [f"RewriteRule ^{re.escape(a)}/?$ {b} [L,R=301]" for a, b in REDIRECCIONES]) or "# (ninguna)"
    red2 = "\n".join(f"RewriteRule ^{re.escape(a)}/?$ {b} [L,R=302]" for a, b in REDIRECCIONES_302) or "# (ninguna)"
    sust = {"__NOMBRE__": N["nombre"], "__DOMINIO__": DOMINIO, "__HOST_SIN_WWW__": host.removeprefix("www."),
            "__HOST__": host, "__CONTACTO__": URLS["contacto"], "__REDIRECCIONES_302__": red2, "__REDIRECCIONES__": red, "__EMAIL__": N["email"],
            "__MAX__": str(FOTO_MAX_MB)}
    h, e = HTACCESS, ENVIAR
    for k, v in sust.items():
        h, e = h.replace(k, v), e.replace(k, v)
    if not host.startswith("www."):
        pass  # dominio sin www: la regla de arriba quita el www
    else:  # dominio con www: se fuerza el www en lugar de quitarlo
        h = h.replace("# Sin www (paso 18)\nRewriteCond %{HTTP_HOST} ^www\\. [NC]", "# Con www (paso 18)\nRewriteCond %{HTTP_HOST} !^www\\. [NC]")
    open(S(".htaccess"), "w").write(h)
    open(S("enviar.php"), "w").write(e)
    # Vista previa en Vercel: nada se indexa en *.vercel.app (en el hosting del cliente manda el .htaccess)
    open(S("vercel.json"), "w").write(json.dumps({"cleanUrls": False, "trailingSlash": True,
        "headers": [{"source": "/(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]}]}, indent=1))


DIAS_N = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}


def js():
    """main.js del cliente con sus datos (horario, festivos, dominio, clave de cookies, textos del estado)."""
    N_ = N
    hosts = "|".join(re.escape(h) for h in HOST_PRODUCCION).replace("\\", "\\\\")
    sust = {"__HOSTS_RE__": hosts, "__COOKIES__": COOKIES_CLAVE, "__TZ__": N_["zona_horaria"],
            "__FESTIVOS__": json.dumps(N_["festivos"]), "__PASCUA__": json.dumps(N_.get("festivos_pascua", [])),
            "__DIAS_N__": json.dumps([DIAS_N[d] for d in N_["dias_schema"]]),
            "__ABRE_H__": str(int(N_["abre"][:2])), "__CIERRA_H__": str(int(N_["cierra"][:2])),
            "__TRAMOS__": json.dumps([[int(a[:2]) * 60 + int(a[3:]), int(c[:2]) * 60 + int(c[3:])] for a, c in N_["tramos"]]),
            "__ESTADO_ABIERTO__": json.dumps(texto("estado_abierto"), ensure_ascii=False),
            "__ESTADO_FUERA__": json.dumps(texto("estado_fuera"), ensure_ascii=False),
            "__PROMESA_ABIERTO__": json.dumps(texto("promesa_abierto"), ensure_ascii=False),
            "__PROMESA_ANTES__": json.dumps(texto("promesa_antes"), ensure_ascii=False),
            "__PROMESA_SIGUIENTE__": json.dumps(texto("promesa_siguiente", dia="{dia}"), ensure_ascii=False)}
    j = open(R("cliente", "js", "main.js"), encoding="utf-8").read()
    for k, v in sust.items():
        j = j.replace(k, v)
    faltan = re.findall(r"__[A-Z_]+__", j)
    if faltan:
        sys.exit(f"main.js: marcadores sin rellenar {faltan}")
    open(S("js", "main.js"), "w", encoding="utf-8").write(j)


def main():
    copiar()
    n = imagenes()
    k = css()
    servidor()
    print(f"rematar: {n} fotos × 4 variantes · estilo.css {k/1024:.1f} KB · v{VERSION}")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""GYF-Archidex · Rematar (paso 52): siempre el ÚLTIMO del build.
Copia recursos, genera imágenes 800/1600 en JPG y WebP, une y minifica el CSS,
y deja los archivos de servidor (.htaccess, enviar.php, favicons, manifest)."""
import os, re, shutil, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import (VERSION, NEGOCIO as N, DOMINIO, MARCA, COOKIES_CLAVE, HOST_PRODUCCION, COLOR_TEMA, URLS, FOTO_MAX_MB, texto)
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
    """Fotos (JPG/PNG/WebP) → 800 y 1600 en JPG y WebP."""
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
    shutil.copy(R("contenido", "resenas.json"), S("resenas.json"))


HTACCESS = r"""# __NOMBRE__ · servidor Apache (hosting del cliente; nginx delante, acepta .htaccess)
Options -Indexes
DirectoryIndex index.html
AddType font/woff2 .woff2
AddType application/manifest+json .webmanifest
AddCharset utf-8 .txt

<FilesMatch "\.(zip|sql|bak|old|log|sh|ini|env|git.*|md|py|csv)$">
  Require all denied
</FilesMatch>
ErrorDocument 404 /404.html
ErrorDocument 410 /404.html

<IfModule mod_rewrite.c>
RewriteEngine On
# Sin www y a https, en un solo salto (Bruno: http://, www. y https://www. → https://solvento.es/ con la misma ruta).
# Las condiciones de X-Forwarded-* evitan el bucle detrás del proxy (lo que tiró la web de Marcos).
RewriteCond %{HTTP_HOST} ^www\. [NC,OR]
RewriteCond %{HTTPS} off
RewriteCond %{HTTP:X-Forwarded-Proto} !https [NC]
RewriteCond %{HTTP:X-Forwarded-SSL} !on [NC]
RewriteRule ^ __DOMINIO__%{REQUEST_URI} [L,R=301,NE]
RewriteCond %{HTTP_HOST} ^www\. [NC]
RewriteRule ^ __DOMINIO__%{REQUEST_URI} [L,R=301,NE]

# 1 · Concretas del mapa de Nuria (02-KEYWORDS-Y-ARQUITECTURA, hoja Mapa 301): primero las 301, después los 410
__R301__
__R410__

# 2 · Reglas por patrón, por este orden (hoja Mapa 301, P1-P13)
RewriteRule ^home/?$ / [L,R=301]
RewriteRule ^(sitemap_index\.xml|wp-sitemap\.xml|[a-z0-9_-]+-sitemap[0-9]*\.xml)$ /sitemap.xml [L,R=301]
RewriteRule ^retirada-amianto/.+$ /retirada-amianto/ [L,R=301]
RewriteRule ^instalar(/.*)?$ /aire-acondicionado/ [L,R=301]
RewriteRule ^instaladores-aire-acondicionado/[^/]+/[^/]+ - [G,L]
RewriteRule ^instaladores-aire-acondicionado(/.*)?$ /aire-acondicionado/ [L,R=301]
RewriteRule ^servicios/[^/]+/.+$ - [G,L]
RewriteRule ^(tag|category|author|portfolio-types)(/.*)?$ - [G,L]
RewriteRule (^|/)feed/?$ - [G,L]
RewriteRule ^comments/feed/?$ - [G,L]
RewriteRule ^(wp-admin|wp-content|wp-includes|wp-json)(/.*)?$ - [G,L]
RewriteRule ^(wp-login\.php|xmlrpc\.php|wp-cron\.php)$ - [G,L]
RewriteCond %{QUERY_STRING} (^|&)(p|page_id|attachment_id|s|cat|tag|author)= [NC]
RewriteRule ^$ - [G,L]
RewriteRule ^.+/page/[0-9]+/?$ - [G,L]
RewriteRule ^(home|empresa|contacto)/.+$ - [G,L]

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
$tipo = ($_POST['tipo'] ?? '') === 'empleo' ? 'empleo' : 'presupuesto';
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
$vuelta = $tipo === 'empleo' ? '/trabaja-con-nosotros/' : '__CONTACTO__';
if ($motivo !== '') { header('Location: ' . $vuelta . '?enviado=0&motivo=' . $motivo . '#form-error'); exit; }
$para = '__EMAIL__';
if ($tipo === 'empleo') {
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
header('Location: ' . $vuelta . '?enviado=' . ($enviado ? '1#form-ok' : '0&motivo=envio#form-error'));
"""


def servidor():
    import json as _j, re as _re
    host = DOMINIO.split("//")[1]
    mapa = _j.load(open(R("generador", "mapa301.json"), encoding="utf-8"))
    r301 = "\n".join(f"RewriteRule ^{_re.escape(a.strip('/'))}/?$ {b} [L,R=301]" for a, b in mapa["r301"] if a != "/")
    r410 = "\n".join(f"RewriteRule ^{_re.escape(a.strip('/'))}/?$ - [G,L]" for a in mapa["r410"])
    sust = {"__NOMBRE__": N["nombre"], "__DOMINIO__": DOMINIO, "__HOST_SIN_WWW__": host.removeprefix("www."),
            "__CONTACTO__": URLS["contacto"], "__R301__": r301, "__R410__": r410, "__EMAIL__": N["email"], "__MAX__": str(FOTO_MAX_MB)}
    h, e = HTACCESS, ENVIAR
    for k, v in sust.items():
        h, e = h.replace(k, v), e.replace(k, v)
    open(S(".htaccess"), "w").write(h)
    # Vista previa en Vercel (paso 23): nada se indexa en *.vercel.app. En el hosting del cliente manda el .htaccess.
    open(S("vercel.json"), "w").write(json.dumps({"cleanUrls": False, "trailingSlash": True,
        "headers": [{"source": "/(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]}]}, indent=1))
    open(S("enviar.php"), "w").write(e)


DIAS_N = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}


def js():
    """main.js del cliente con sus datos (tramos de horario, festivos, dominio, clave de cookies, textos del estado)."""
    hosts = "|".join(re.escape(h) for h in HOST_PRODUCCION).replace("\\", "\\\\")
    mins = lambda x: int(x[:2]) * 60 + int(x[3:])
    sust = {"__HOSTS_RE__": hosts, "__COOKIES__": COOKIES_CLAVE, "__TZ__": N["zona_horaria"],
            "__FESTIVOS__": json.dumps(N["festivos"]), "__PASCUA__": json.dumps(N.get("festivos_pascua", [])),
            "__DIAS_N__": json.dumps([DIAS_N[d] for d in N["dias_schema"]]),
            "__TRAMOS__": json.dumps([[mins(a), mins(c)] for a, c in N["tramos"]]),
            "__ESTADO_ABIERTO__": json.dumps(texto("estado_abierto"), ensure_ascii=False),
            "__ESTADO_FUERA__": json.dumps(texto("estado_fuera"), ensure_ascii=False)}
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

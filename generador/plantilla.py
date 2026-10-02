# -*- coding: utf-8 -*-
"""GYF-Archidex · Plantilla común: <head>, cabecera (opción B: menú en línea, teléfono y botón), menú del móvil,
pie verde noche (opción C) y piezas reutilizables (iconos, botones, fotos, estado)."""
import html, json, os, re
from config import (VERSION, DOMINIO, GTM_ID, NEGOCIO as N, MENU, LEGALES, CREDITO, MARCA, URLS, COLOR_TEMA,
                    FICHA, FUENTES_PRECARGA, texto)

A = lambda s: html.escape(str(s), quote=True)
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------- Iconos (recursos/iconos/sprite.svg) ----------
_SP = open(os.path.join(RAIZ, "recursos", "iconos", "sprite.svg"), encoding="utf-8").read()
SIMBOLOS = {m.group(1): m.group(0) for m in re.finditer(r'<symbol id="i-([a-z0-9-]+)".*?</symbol>', _SP, re.S)}


def sprite(html_pagina):
    usados = sorted(set(re.findall(r'href="#i-([a-z0-9-]+)"', html_pagina)))
    faltan = [u for u in usados if u not in SIMBOLOS]
    if faltan:
        raise SystemExit(f"plantilla: iconos que no están en recursos/iconos/sprite.svg: {faltan}")
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">'
            + "".join(SIMBOLOS[u] for u in usados) + "</svg>")


def ico(nombre, clase=""):
    return f'<svg class="ico {clase}" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><use href="#i-{nombre}"/></svg>'


# ---------- Botones (opción B: cuadrado en verde; secundario negro) ----------
def boton(t, href, clase="", icono="flecha-diagonal", extra=""):
    ic = ico(icono, "btn__ico") if icono else ""
    return f'<a class="btn {clase}" href="{A(href)}"{extra}><span>{html.escape(t)}</span>{ic}</a>'


def btn_foto(clase="", zona=""):
    z = f' data-zona="{zona}"' if zona else ""
    return boton(texto("boton"), URLS["contacto"] + "#presupuesto", clase, "flecha-diagonal", z)


def tel(clase="", zona="", texto_t=None):
    z = f' data-zona="{zona}"' if zona else ""
    return f'<a class="tel {clase}" href="tel:{N["telefono_e164"]}"{z}>{texto_t or N["telefono"]}</a>'


# ---------- Fotos (rematar.py genera 800 y 1600 en JPG y WebP) ----------
def medida(archivo):
    from PIL import Image
    r = os.path.join(RAIZ, "recursos", "fotos", archivo)
    if os.path.exists(r):
        with Image.open(r) as im:
            return im.width, im.height
    raise SystemExit(f"plantilla: falta la foto recursos/fotos/{archivo}")


def foto(archivo, alt, sizes="(max-width: 900px) 100vw, 50vw", prioridad=False, clase=""):
    base = archivo.rsplit(".", 1)[0]
    w, h = medida(archivo)
    alto = round(1600 * h / w)
    carga = 'fetchpriority="high"' if prioridad else 'loading="lazy" decoding="async"'
    return (f'<picture class="{clase}"><source type="image/webp" srcset="/img/{base}-800.webp 800w, /img/{base}-1600.webp 1600w" sizes="{sizes}">'
            f'<img src="/img/{base}-1600.jpg" srcset="/img/{base}-800.jpg 800w, /img/{base}-1600.jpg 1600w" sizes="{sizes}" '
            f'width="1600" height="{alto}" alt="{A(alt)}" {carga}></picture>')


def estado(clase=""):
    return f'<p class="estado {clase}" data-estado><i></i><span>{N["horario_corto"]}</span></p>'


# ---------- <head> ----------
def cabeza(p, schema, robots="index, follow", precarga=None):
    url = DOMINIO + p["url"]
    pre = ""
    if precarga:
        pre = f'<link rel="preload" as="image" type="image/webp" imagesrcset="{precarga[0]}" imagesizes="{precarga[1]}" fetchpriority="high">'
    fuentes = "".join(f'<link rel="preload" href="/fuentes/{f}" as="font" type="font/woff2" crossorigin>' for f in FUENTES_PRECARGA)
    return f"""<!doctype html>
<html lang="es" data-gtm="{GTM_ID}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{A(p['title'])}</title>
<meta name="description" content="{A(p['meta'])}">
<meta name="robots" content="{robots}">
{"" if p["url"] == "/404/" else f'<link rel="canonical" href="{url}">'}
<meta name="theme-color" content="{COLOR_TEMA}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{A(N['nombre'])}">
<meta property="og:title" content="{A(p['title'])}">
<meta property="og:description" content="{A(p['meta'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMINIO}/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
{fuentes}
{pre}
<link rel="stylesheet" href="/css/estilo.css?v={VERSION}">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(",", ":"))}</script>
</head>
"""


# ---------- Cabecera (opción B) y menú del móvil ----------
def _cur(u, actual):
    return ' aria-current="page"' if u == actual else ""


def cabecera(actual):
    nav = []
    for nombre, dest in MENU:
        if isinstance(dest, list):
            li = "".join(f'<li><a href="{u}"{_cur(u, actual)}>{n}</a></li>' for n, u in dest)
            dentro = any(u == actual for _, u in dest)
            nav.append(f'<li class="nav__grupo"><button type="button" class="nav__abre{" activo" if dentro else ""}" aria-expanded="false">{nombre}<span aria-hidden="true">+</span></button><ul class="nav__sub">{li}</ul></li>')
        else:
            nav.append(f'<li><a href="{dest}"{_cur(dest, actual)}>{nombre}</a></li>')
    logo = f'<img src="/marca/{MARCA["logo"]}" alt="{A(texto("logo_alt"))}" width="{MARCA["logo_ancho"]}" height="{MARCA["logo_alto"]}">'
    movil = []
    for nombre, dest in MENU:
        if isinstance(dest, list):
            movil.append(f'<li class="menu__h">{nombre}</li>' + "".join(f'<li><a href="{u}"{_cur(u, actual)}>{n}</a></li>' for n, u in dest))
        else:
            movil.append(f'<li><a class="menu__grande" href="{dest}"{_cur(dest, actual)}>{nombre}</a></li>')
    return f"""<body>
<!--SPRITE-->
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="cab" data-cab>
 <div class="c cab__in">
  <a class="cab__logo" href="/" aria-label="{A(N['nombre'])}: inicio">{logo}</a>
  <nav class="nav" aria-label="Principal"><ul>{"".join(nav)}</ul></nav>
  <a class="cab__tel tel" href="tel:{N['telefono_e164']}" data-zona="cabecera"><small>{texto("cab_horario")}</small>{N['telefono']}</a>
  {btn_foto("cab__btn", "cabecera")}
  <button class="cab__burger" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="menu"><span></span><span></span></button>
 </div>
</header>
<div class="menu" id="menu" aria-hidden="true" role="dialog" aria-label="Menú" data-menu>
 <div class="c menu__in">
  <div class="menu__top"><img src="/marca/{MARCA['logo_blanco']}" alt="" width="{MARCA['logo_ancho']}" height="{MARCA['logo_alto']}"><button class="menu__cerrar" type="button" aria-label="Cerrar menú">{ico("cerrar")}</button></div>
  <nav aria-label="Menú del móvil"><ul class="menu__lista"><li><a class="menu__grande" href="/"{_cur("/", actual)}>Inicio</a></li>{"".join(movil)}</ul></nav>
  <div class="menu__contacto">{estado("estado--claro")}<a class="menu__tel tel" href="tel:{N['telefono_e164']}">{N['telefono']}</a><a href="mailto:{N['email']}">{N['email']}</a></div>
 </div>
</div>
<main id="contenido">
"""


# ---------- Pie (opción C): verde noche, frase de cierre gigante y teléfono; «solvento» en trazo al fondo ----------
def pie():
    def lista(L):
        return "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in L)
    com = next(d for n, d in MENU if n == "Comunidades")
    par = next(d for n, d in MENU if n == "Particulares")
    sol = [("Administradores de fincas", "/administradores-de-fincas/"), ("Empresa", "/empresa/"),
           ("Trabaja con nosotros", "/trabaja-con-nosotros/"), ("Contacto", "/contacto/")]
    leg = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in LEGALES)
    return f"""</main>
<footer class="pie">
 <div class="c">
  <div class="pie__grande">
   <p class="pie__frase">{texto("pie_frase")}</p>
   <div class="pie__llamar"><small>{texto("pie_horario")}</small>{tel("pie__tel", "pie")}{btn_foto("btn--claro", "pie")}</div>
  </div>
  <div class="pie__cols">
   <div><p class="pie__h">{N['nombre']}</p><address><a href="{FICHA}" rel="noopener" target="_blank">{N['calle']}<br>{N['zona_calle']}<br>{N['cp']} {N['localidad']} ({N['provincia']})</a><br><a href="mailto:{N['email']}">{N['email']}</a><br>Oficina: <a class="tel" href="tel:{N['oficina_e164']}">{N['oficina']}</a></address>{estado("estado--claro")}</div>
   <div><p class="pie__h">Comunidades</p><ul>{lista(com)}</ul></div>
   <div><p class="pie__h">Particulares</p><ul>{lista(par)}</ul><p class="pie__h pie__h--2">Solvento</p><ul>{lista(sol)}</ul></div>
   <div><p class="pie__h">Habilitaciones</p><ul><li>RERA n.º {N['rera']}</li><li>Gas · Climatización · RITE</li><li>Baja tensión</li><li>RC 1,3 M€ con MAPFRE</li></ul></div>
  </div>
  <div class="pie__base">
   <img src="/marca/{MARCA['logo_blanco']}" alt="{A(N['nombre'])}" width="{MARCA['logo_ancho']}" height="{MARCA['logo_alto']}" loading="lazy">
   <ul>{leg}<li><a href="#" data-cookies-config>Configurar cookies</a></li></ul>
   <span>© <span data-anio>2026</span> {N['razon_social']} · Diseño y SEO: <a href="{CREDITO[1]}" target="_blank" rel="noopener">{CREDITO[0]}</a></span>
  </div>
 </div>
 <img class="pie__agua" src="/marca/{MARCA['logo_trazo']}" alt="" width="{MARCA['logo_ancho']}" height="{MARCA['logo_alto']}" loading="lazy">
</footer>
<nav class="barra-movil" aria-label="Contacto rápido"><a class="tel" href="tel:{N['telefono_e164']}" data-zona="barra">{ico("telefono")}Llamar</a><a href="{URLS['contacto']}#presupuesto" data-zona="barra">{ico("camara")}{texto("boton_corto")}</a></nav>
<div class="cookies" id="cookies" role="dialog" aria-label="Aviso de cookies">
 <p>{texto("cookies")} <a href="/cookies/">Política de cookies</a>.</p>
 <div class="acciones"><button class="btn btn--peq" type="button" data-cookies="si"><span>Aceptar</span></button><button class="btn btn--linea btn--peq" type="button" data-cookies="no"><span>Rechazar</span></button></div>
</div>
<script src="/js/main.js?v={VERSION}" defer></script>
</body>
</html>
"""

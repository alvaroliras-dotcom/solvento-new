# -*- coding: utf-8 -*-
"""GYF-Archidex · Genera sitio/ entero a partir de contenido/. Orden: build.py → rematar.py → controles.py.

Piezas de Archidex (007 de la biblioteca, FICHA.md) con las opciones de la firma de Solvento
(07-FIRMA-GRAFICA/FIRMA.md) sobre la base GYF: schema, sitemap, llms.txt, estado en vivo, reseñas literales,
FAQ, mapa por CID, cookies y GTM. Dónde está cada pieza: 007-ARCHIDEX/MAPA-DEL-TEMA.md."""
import html, json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import datos
from datos import inline, esc
A = lambda x: html.escape(str(x), quote=True)
from config import (DOMINIO, NEGOCIO as N, URLS, MUNICIPIOS, NOMBRE_CORTO, MADRE, CONTACTO_INDEXABLE, PORTADA_FOTO, LEGALES,
                    LLMS_PRINCIPALES, TEXTOS, FICHA, MARCA, SELLOS, SELLOS_NOTA, ESTRELLA_FRASE, ESTRELLA_CLAVE,
                    ESTRELLA_BOTON, ESTRELLA_TARJETAS, FILAS_FOTO, PROPIA, CIFRAS, CIFRAS_TITULO, PAPELES_ICONOS,
                    PIEZAS_H2, TEMAS, QUIEN, FOTO_MAX_MB, RESENAS, texto)
import plantilla as T

RAIZ = datos.RAIZ
SITIO = os.path.join(RAIZ, "sitio")
PAGINAS = datos.todas()
POR_URL = {p["url"]: p for p in PAGINAS}
PUEBLO = dict(MUNICIPIOS)
ALT = json.load(open(os.path.join(RAIZ, "generador", "alt_fotos.json"), encoding="utf-8"))
NOMBRE_CORTO = dict(NOMBRE_CORTO)

R_FOTO = re.compile(r"^\(FOTO:\s*(.+?)\s+—\s+([a-z0-9-]+\.jpg)\)\s*$")
R_OPINION = re.compile(r"^\(Bloque de opiniones de Google[^)]*?n\.º\s*(\d+)")
R_FRAG = re.compile(r"(?:Fragmento|Texto) literal:\s*«(.+)»\)\s*$")
R_MAPA = re.compile(r"^\(Mapa de Google")
R_FORM = re.compile(r"^(\*\*Formulario:\*\*|\[Botón\]|Línea informativa|\*\*Soy )")


def nombre(url):
    return NOMBRE_CORTO.get(url) or PUEBLO.get(url) or url.strip("/")


def migas(url):
    if url == "/":
        return []
    cad = [("/", "Inicio")]
    m = MADRE.get(url)
    while m:
        cad.insert(1, (m, nombre(m)))
        m = MADRE.get(m)
    cad.append((url, nombre(url)))
    return cad


def migas_html(url):
    c = migas(url)
    if not c:
        return ""
    li = [f'<li><a href="{u}">{esc(n)}</a></li>' if i < len(c) - 1 else f'<li aria-current="page">{esc(n)}</li>' for i, (u, n) in enumerate(c)]
    return f'<nav class="migas" aria-label="Migas de pan"><div class="c"><ol>{"".join(li)}</ol></div></nav>'


# ---------- Schema ----------
NEG_ID = DOMINIO + "/#negocio"


def negocio_schema():
    d = {
        "@type": N["schema_tipo"], "@id": NEG_ID, "name": N["nombre"], "alternateName": N["nombre_largo"],
        "legalName": N["razon_social"], "taxID": N["cif"], "url": DOMINIO + "/", "telephone": N["telefono_e164"],
        "email": N["email"], "logo": DOMINIO + "/marca/" + MARCA["gota"], "image": DOMINIO + "/og-image.jpg",
        "address": {"@type": "PostalAddress", "streetAddress": f"{N['calle']}, {N['zona_calle']}", "postalCode": N["cp"],
                    "addressLocality": N["localidad"], "addressRegion": N["region"], "addressCountry": "ES"},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": N["dias_schema"], "opens": a, "closes": c}
                                      for a, c in N["tramos"]],
        "areaServed": [{"@type": "AdministrativeArea", "name": "Comunidad de Madrid"}] + [{"@type": "City", "name": n} for _, n in MUNICIPIOS],
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": N["valoracion"].replace(",", "."),
                            "reviewCount": int(N["resenas"]), "bestRating": "5", "worstRating": "1"},
        "geo": {"@type": "GeoCoordinates", "latitude": N["lat"], "longitude": N["lng"]},
        "hasMap": FICHA, "sameAs": [FICHA], "knowsAbout": N["knows_about"],
        "hasCredential": [{"@type": "EducationalOccupationalCredential", "name": "Registro de Empresas con Riesgo por Amianto (RERA) de la Comunidad de Madrid",
                           "identifier": N["rera"]}],
    }
    return d


def schema_de(p):
    url = DOMINIO + p["url"]
    g = [negocio_schema(),
         {"@type": "WebPage", "@id": url + "#pagina", "url": url, "name": p["title"], "description": p["meta"], "inLanguage": "es",
          "isPartOf": {"@id": DOMINIO + "/#web"}, "about": {"@id": NEG_ID}, **({"dateModified": p["mod"]} if p.get("mod") else {})},
         {"@type": "WebSite", "@id": DOMINIO + "/#web", "url": DOMINIO + "/", "name": N["nombre"], "inLanguage": "es", "publisher": {"@id": NEG_ID}}]
    c = migas(p["url"])
    if c:
        g.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMINIO + u} for i, (u, n) in enumerate(c)]})
    t = datos.tipo_de(p["url"])
    if t in ("servicio", "municipio"):
        area = {"@type": "City", "name": PUEBLO[p["url"]]} if t == "municipio" else {"@type": "AdministrativeArea", "name": "Comunidad de Madrid"}
        g.append({"@type": "Service", "name": p["h1"], "serviceType": p["keyword"] or N["servicio_tipo"], "provider": {"@id": NEG_ID},
                  "url": url, "areaServed": area})
    if p["faq"]:
        g.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plano(a)}} for q, a in p["faq"]]})
    return {"@context": "https://schema.org", "@graph": g}


# ---------- Utilidades ----------
def plano(txt):
    return re.sub(r"<[^>]+>", "", inline(txt))


def slug(t):
    import unicodedata
    s = unicodedata.normalize("NFKD", plano(t)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:48] or "seccion"


def clave(t, k):
    """Opción C de la firma: la palabra clave del titular va en verde (en turquesa sobre oscuro)."""
    t = esc(t)
    if k and esc(k) in t:
        return t.replace(esc(k), f'<span class="k">{esc(k)}</span>', 1)
    return t


def h2_clave(t):
    """H2 en forma de pregunta: la segunda mitad (desde la última coma o tras el verbo) en verde."""
    pt = plano(t)
    w = pt.rstrip("?").split()
    if len(w) < 3:
        return esc(pt)
    k = " ".join(w[len(w) // 2 + (len(w) % 2):]) + ("?" if pt.endswith("?") else "")
    return clave(pt, k)


def secciones(bl):
    intro, secs, act = [], [], None
    for b in bl:
        if b[0] == "h2":
            act = {"h2": b[1], "bl": []}; secs.append(act)
        elif act is None:
            intro.append(b)
        else:
            act["bl"].append(b)
    return intro, secs


PENDIENTES = set()


def hay_foto(f):
    ok = os.path.exists(os.path.join(RAIZ, "recursos", "fotos", f))
    if not ok:
        PENDIENTES.add(f)
    return ok


def fotos_de(bl):
    return [R_FOTO.match(c).group(2) for t, c in bl if t == "p" and R_FOTO.match(c) and hay_foto(R_FOTO.match(c).group(2))]


def ancha(f):
    """Solo una foto de 1.200 px o más va a la cabecera a sangre."""
    return T.medida(f)[0] >= 1200


def alt(archivo):
    if archivo not in ALT:
        raise SystemExit(f"build: falta el texto alternativo de {archivo} en generador/alt_fotos.json")
    return ALT[archivo]


def foto(archivo, sizes="(max-width: 900px) 100vw, 60vw", clase="", prioridad=False):
    return T.foto(archivo, alt(archivo), sizes, prioridad, clase)


USADAS = set()   # fotos ya puestas en la página (cabecera y entrada): no se repiten en el cuerpo

# ---------- Bloques de texto → HTML ----------
SOLO_ENLACE = re.compile(r"^\s*\[(?:LINK )?[^\]]+\]\([^)]+\)\s*(🔗|🆕)?\s*$")
NEGRITA_INICIO = re.compile(r"^\*\*(.+?)\*\*[,.:]?\s*(.*)$")


def lista_html(items):
    """Lista con negrita al principio → «papeles» con check y línea (piezas de la ficha de servicio)."""
    if all(NEGRITA_INICIO.match(x) for x in items):
        li = []
        for x in items:
            m = NEGRITA_INICIO.match(x)
            li.append(f'<li class="rv">{T.ico("check")}<span><strong>{inline(m.group(1))}</strong> {inline(m.group(2))}</span></li>')
        return f'<ul class="papeles">{"".join(li)}</ul>'
    if all(SOLO_ENLACE.match(x) for x in items):
        li = []
        for x in items:
            m = re.search(r"\[(?:LINK )?([^\]]+)\]\(([^)]+)\)", x)
            li.append(f'<li><a href="{m.group(2)}"><span>{esc(m.group(1))}</span><i>{T.ico("flecha-diagonal")}</i></a></li>')
        return f'<ul class="enlaces">{"".join(li)}</ul>'
    return '<ul class="lista">' + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"


def pasos_html(items):
    out = []
    for i, it in enumerate(items, 1):
        m = NEGRITA_INICIO.match(it)
        if m and m.group(2)[:1].isupper():
            tit, txt = inline(m.group(1)).rstrip("."), inline(m.group(2))
        else:
            tit, txt = inline(it), ""
        out.append(f'<li class="paso rv"><span class="paso__n">({i:02d})</span><h3 class="paso__tit">{tit}</h3>'
                   f'{f"<p class=paso__txt>{txt}</p>" if txt else ""}</li>')
    return f'<ol class="pasos" data-n="{len(items):02d}">{"".join(out)}</ol>'


def tabla_html(cab, filas):
    vacia = all(not plano(h) for h in cab)
    th = "" if vacia else "<thead><tr>" + "".join(f'<th scope="col">{inline(h)}</th>' for h in cab) + "</tr></thead>"
    trs = []
    for f in filas:
        f = (f + [""] * len(cab))[:len(cab)]
        celdas = []
        for k, (h, c) in enumerate(zip(cab, f)):
            tag = "th" if (vacia and k == 0) else "td"
            sc = ' scope="row"' if tag == "th" else ""
            celdas.append(f'<{tag}{sc} data-col="{A(plano(h))}">{inline(c)}</{tag}>')
        trs.append("<tr>" + "".join(celdas) + "</tr>")
    return f'<div class="tabla rv"><table>{th}<tbody>{"".join(trs)}</tbody></table></div>'


FRAG = {}   # n.º de reseña → fragmento literal elegido en el texto («Fragmento literal: «…»»)


def opinion_html(n, clase=""):
    o = RESENAS.get(int(n))
    if not o:
        raise SystemExit(f"build: la reseña n.º {n} no está en contenido/resenas.json")
    txt = FRAG.get(int(n)) or " ".join(o["texto"].split())
    if FRAG.get(int(n)) and plano(FRAG[int(n)]).rstrip(".") not in " ".join(o["texto"].split()):
        raise SystemExit(f"build: el fragmento de la reseña n.º {n} no es literal")
    return f"""<figure class="opinion rv {clase}">
 <span class="opinion__comillas" aria-hidden="true">“</span>
 <blockquote><p>{esc(txt)}</p></blockquote>
 <figcaption><strong>{esc(o['nombre'])}</strong><a href="{FICHA}" rel="noopener" target="_blank">{esc(texto("opinion_fuente"))}</a></figcaption>
</figure>"""


MAPA_EMBED = f"https://maps.google.com/maps?cid={N['cid']}&z=15&hl=es&output=embed"


def mapa_html():
    return (f'<div class="mapa rv"><iframe src="{MAPA_EMBED}" title="Mapa: {A(N["nombre"])}, {A(N["calle"])}, {A(N["localidad"])}" '
            f'loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>'
            f'<a class="mapa__ir" href="{FICHA}" rel="noopener" target="_blank">Ver la ficha en Google Maps {T.ico("flecha-diagonal")}</a></div>')


def render(bl, url=""):
    """Markdown en bloques → HTML del cuerpo de una sección. Las fotos seguidas van en pareja."""
    out, i = [], 0
    while i < len(bl):
        t, c = bl[i]
        if t == "p":
            if R_FOTO.match(c):
                grupo = []
                while i < len(bl) and bl[i][0] == "p" and R_FOTO.match(bl[i][1]):
                    g = R_FOTO.match(bl[i][1]).group(2); i += 1
                    if hay_foto(g) and g not in USADAS:
                        grupo.append(g)
                if not grupo:
                    continue
                USADAS.update(grupo)
                if len(grupo) > 1:
                    out.append('<div class="pareja">' + "".join(f'<figure class="rv">{foto(g, "(max-width: 900px) 100vw, 30vw")}</figure>' for g in grupo) + "</div>")
                else:
                    out.append(f'<figure class="foto-sec rv">{foto(grupo[0])}</figure>')
                continue
            if R_OPINION.match(c):
                fr = R_FRAG.search(c)
                if fr:
                    FRAG[int(R_OPINION.match(c).group(1))] = fr.group(1)
                out.append(opinion_html(R_OPINION.match(c).group(1)))
            elif R_MAPA.match(c):
                out.append(mapa_html())
            elif R_FORM.match(c):
                pass  # la especificación del formulario: el formulario lo pone la página
            else:
                out.append(f'<p class="rv">{inline(c)}</p>')
        elif t in ("h3", "h4"):
            out.append(f'<h3 class="h3 rv">{inline(c)}</h3>')
        elif t == "ul":
            out.append(lista_html(c))
        elif t == "ol":
            out.append(pasos_html(c))
        elif t == "tabla":
            out.append(tabla_html(*c))
        i += 1
    return "\n".join(out)


# ---------- Piezas de la portada (firma §2) ----------
def cinta_html():
    its = ["Bajantes de amianto", "Fontanería del edificio", "Cubiertas y terrazas", "Trabajos verticales", "Gas y calefacción", "RERA 2800625"]
    gota = f'<img class="cinta__gota" src="/marca/{MARCA["gota_turquesa"]}" alt="" width="357" height="531">'
    grupo = "".join(f'<span class="cinta__it{" cinta__it--hueco" if i % 2 else ""}">{esc(t)}</span>{gota}' for i, t in enumerate(its))
    return f'<div class="cinta" aria-hidden="true"><div class="cinta__pista" data-cinta><div class="cinta__grupo">{grupo}</div><div class="cinta__grupo">{grupo}</div></div></div>\n'


def portada_home(p):
    if PORTADA_FOTO:
        fondo = (f'<div class="banda-marca banda-marca--foto">\n   {foto(PORTADA_FOTO, "(max-width: 1240px) 100vw, 1200px", "banda-marca__foto", prioridad=True)}'
                 '\n   <span class="banda-marca__velo" aria-hidden="true"></span>')
    else:
        fondo = (f'<div class="banda-marca">\n   <span class="banda-marca__azulejo" aria-hidden="true"></span>'
                 f'\n   <img class="banda-marca__gota" src="/marca/{MARCA["gota_blanca"]}" alt="" width="357" height="531">'
                 f'\n   <img class="banda-marca__centro" src="/marca/{MARCA["gota_turquesa"]}" alt="" width="357" height="531">')
    sellos = "".join(f'<div class="sello"><b>{esc(v)}</b><span>{esc(t)}</span></div>' for v, t in SELLOS)
    return f"""<section class="portada" aria-labelledby="h1">
 <div class="reticula" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
 <div class="c">
  <div class="portada__fila">
   <div>
    <p class="pildora">{esc(p['etiqueta'])}</p>
    <h1 id="h1" class="h1-home">{clave(p['h1'], 'sur de Madrid')}</h1>
   </div>
   <div class="portada__der">
    <p>{inline(p['entrada_corta'])}</p>
    <div class="acciones">{T.btn_foto("", "portada")}</div>
    <p class="portada__tel">o llame al {T.tel("", "portada", f"<b>{N['telefono']}</b>")}</p>
   </div>
  </div>
  {fondo}
   <p class="banda-marca__nota">{esc(SELLOS_NOTA)}</p>
   <div class="banda-marca__sellos">{sellos}</div>
  </div>
 </div>
</section>
"""


def estrella(dec):
    tarj = "".join(f'<a class="tarjeta rv" href="{ESTRELLA_BOTON[1]}">{T.foto(f, a, "(max-width: 900px) 100vw, 33vw")}'
                   f'<span class="tarjeta__et">{esc(e)}</span><span class="tarjeta__fl">{T.ico("flecha-diagonal")}</span><span class="tarjeta__tit">{esc(t)}</span></a>'
                   for e, t, f, a in ESTRELLA_TARJETAS)
    return f"""<section class="estrella">
 <div class="c">
  <p class="frase rv">{clave(ESTRELLA_FRASE, ESTRELLA_CLAVE)}</p>
  <div class="estrella__pie">
   <span></span>
   <div class="prosa rv">{"".join(f"<p>{inline(x)}</p>" for x in dec)}</div>
   <div class="estrella__btn">{T.boton(ESTRELLA_BOTON[0], ESTRELLA_BOTON[1], "btn--negro")}</div>
  </div>
  <div class="tarjetas">{tarj}</div>
 </div>
</section>
"""


def filas_serv(sec):
    """service-6 (opción A): la tabla «Trabajo | Qué incluye» del texto → filas con número, foto en estadio,
    título con la palabra clave en verde, texto y flecha."""
    tabla = next((c for t, c in sec["bl"] if t == "tabla"), None)
    ps = [c for t, c in sec["bl"] if t == "p" and not R_FOTO.match(c)]
    filas = []
    for i, (trab, inc) in enumerate(tabla[1] if tabla else [], 1):
        m = re.search(r"\[(?:LINK )?([^\]]+)\]\(([^)]+)\)", trab)
        tit, u = (m.group(1), m.group(2)) if m else (plano(trab), None)
        f, k = FILAS_FOTO.get(u, (None, None))
        est = f'<span class="fila__foto">{T.foto(f, "", "260px")}</span>' if f else '<span class="fila__foto fila__foto--vacia"></span>'
        flecha = '<svg class="fila__fl" viewBox="0 0 56 56" aria-hidden="true"><path d="M4 52 52 4M16 4h36v36"/></svg>'
        filas.append(f'<li class="rv"><a class="fila" href="{u}"><span class="fila__n">{i:02d}.</span>{est}'
                     f'<h3 class="fila__tit">{clave(tit, k)}</h3><p class="fila__txt">{inline(inc)}</p>{flecha}</a></li>')
    ps = [x for x in ps if not plano(x).endswith(":") and not plano(x).startswith(ESTRELLA_FRASE)]
    lead = f'<p class="servicios__lead">{inline(ps[0])}</p>' if ps else ""
    resto = ""
    return f"""<section class="servicios" id="{slug(sec['h2'])}">
 <div class="c">
  <div class="servicios__cab">
   <p class="rotulo" aria-hidden="true"><i></i></p>
   <h2 class="h2-rotulo">{esc(plano(sec['h2']))}</h2>
   {T.boton("Para administradores de fincas", URLS["admin"], "btn--enlace", None)}
  </div>
  {lead}
  <ol class="filas">{"".join(filas)}</ol>
  {f'<div class="servicios__resto prosa">{resto}</div>' if resto else ""}
 </div>
</section>
"""


def opinion_y_cifras(n):
    cif = "".join(f'<div class="cifra rv"><b>{esc(v)}</b><span>{esc(t)}</span></div>' for v, t in CIFRAS)
    return f"""<section class="opiniones" aria-label="Opinión publicada en Google">
 <div class="c">
  {opinion_html(n, "opinion--grande")}
  <p class="fantasma" aria-hidden="true" data-t="{A(texto("opiniones_fantasma"))}"></p>
  <div class="cifras"><p class="cifras__tit">{clave(*CIFRAS_TITULO)}</p>{cif}</div>
 </div>
</section>
"""


def papeles(sec):
    """Hueco de los logotipos de Archidex: la lista de papeles del texto en una tira de celdas con icono."""
    ul = next((c for t, c in sec["bl"] if t == "ul"), [])
    celdas = []
    for i, x in enumerate(ul):
        m = NEGRITA_INICIO.match(x)
        tit, txt = (m.group(1), m.group(2)) if m else (x, "")
        ic = PAPELES_ICONOS[i] if i < len(PAPELES_ICONOS) else "check"
        celdas.append(f'<li class="rv">{T.ico(ic)}<b>{inline(tit.rstrip(".:"))}</b><span>{inline(txt)}</span></li>')
    ps = [c for t, c in sec["bl"] if t == "p" and not (R_FOTO.match(c) or R_OPINION.match(c) or R_MAPA.match(c))]
    return f"""<section class="papeles-sec" id="{slug(sec['h2'])}">
 <div class="c">
  <h2 class="h2 rv">{h2_clave(sec['h2'])}</h2>
  {f'<p class="papeles-sec__lead rv">{inline(ps[0])}</p>' if ps else ""}
 </div>
 <ul class="tira" style="--n:{len(celdas)}">{"".join(celdas)}</ul>
 <div class="c">{"".join(f'<p class="papeles-sec__pie rv">{inline(x)}</p>' for x in ps[1:])}</div>
</section>
"""


def propia(txt):
    g, ga = PROPIA["grande"]
    pq, pa = PROPIA["pequena"]
    return f"""<section class="propia">
 <div class="c propia__in">
  <div class="propia__grande rv">{T.foto(g, ga, "(max-width: 900px) 100vw, 40vw")}</div>
  <div class="propia__txt">
   <p class="frase rv">{clave(PROPIA["frase"], PROPIA["clave"])}</p>
   <div class="propia__bajo">
    <p class="rv">{inline(txt.replace(PROPIA["frase"], "").strip())}</p>
    <div class="propia__peq rv">{T.foto(pq, pa, "240px")}</div>
   </div>
  </div>
 </div>
</section>
"""


def puntos(sec, f, a):
    """work-6 (opción A): foto fija a la izquierda y los párrafos de la sección como puntos en círculo."""
    ps = [c for t, c in sec["bl"] if t == "p" and not R_FOTO.match(c)]
    pts = []
    for i, x in enumerate(ps, 1):
        txt = inline(x)
        m = re.match(r"(.+?[.?!])\s+(.+)$", plano(x))
        if m and len(m.group(1)) < 90:
            corte = txt.find(m.group(2)[:20]) if m.group(2)[:20] in txt else -1
            tit, cu = (txt[:corte].strip(), txt[corte:]) if corte > 0 else (txt, "")
        else:
            tit, cu = txt, ""
        pts.append(f'<li class="punto rv"><span class="punto__n">{i:02d}</span><div><h3 class="punto__tit">{tit}</h3>{f"<p>{cu}</p>" if cu else ""}</div></li>')
    return f"""<section class="lunes" id="{slug(sec['h2'])}">
 <div class="c">
  <h2 class="h2 rv">{h2_clave(sec['h2'])}</h2>
  <div class="lunes__dos">
   <div class="lunes__foto"><div class="lunes__fija">{T.foto(f, a, "(max-width: 900px) 100vw, 45vw")}</div></div>
   <ol class="puntos">{"".join(pts)}</ol>
  </div>
 </div>
</section>
"""


def zona(sec, f, a):
    """blog-6: destacado con foto a la izquierda; a la derecha, los enlaces del texto en lista con flecha."""
    ps = [c for t, c in sec["bl"] if t == "p" and not R_FOTO.match(c)]
    enl, txt = [], []
    for x in ps:
        links = re.findall(r"\[(?:LINK )?([^\]]+)\]\(([^)]+)\)", x)
        txt.append(x)
        for tt, u in links:
            if u != URLS["contacto"]:
                enl.append((tt, u, x))
    vistos, li = set(), []
    for tt, u, x in enl:
        if u in vistos:
            continue
        vistos.add(u)
        tit = nombre(u)
        sub = "" if plano(tt).lower() in tit.lower() else f"<small>{esc(tt)}</small>"
        li.append(f'<li><a href="{u}"><span><b>{esc(tit)}</b>{sub}</span><i>{T.ico("flecha-diagonal")}</i></a></li>')
    return f"""<section class="zona" id="{slug(sec['h2'])}">
 <div class="c">
  <h2 class="h2 rv">{h2_clave(sec['h2'])}</h2>
  <div class="zona__dos">
   <div class="zona__dest rv">{T.foto(f, a, "(max-width: 900px) 100vw, 55vw")}<div class="prosa">{"".join(f"<p>{inline(x)}</p>" for x in txt)}</div></div>
   <div><ul class="enlaces enlaces--zona">{"".join(li)}</ul><div class="acciones">{T.btn_foto("", "zona")}</div></div>
  </div>
 </div>
</section>
"""


def faq_html(faq, enlace=True):
    if not faq:
        return ""
    items = "".join(f'<details class="rv" name="faq"{" open" if i == 1 else ""}><summary><span class="faq__n">{i:02d}</span><span>{esc(q)}</span><i aria-hidden="true"></i></summary>'
                    f'<div class="faq__resp"><p>{inline(a)}</p></div></details>' for i, (q, a) in enumerate(faq, 1))
    en = texto("faq_enlace")
    ir = f'<a class="enlace" href="{en[1]}">{esc(en[0])}</a>' if enlace else ""
    return f"""<section class="faq" id="preguntas">
 <div class="c faq__in">
  <div class="faq__tarj rv">
   <p class="faq__et">{esc(texto("faq_etiqueta"))}</p>
   <h2 class="faq__tit">{esc(texto("faq_tarjeta"))}</h2>
   {T.tel("faq__tel", "faq")}
   {ir}
  </div>
  <div class="faq__lista">{items}</div>
 </div>
</section>
"""


# ---------- Interiores ----------
CTA_PAGINA = {"/trabaja-con-nosotros/": ("Apuntarme", "#presupuesto")}


def cab_int(p, t, foto_cab):
    cta = CTA_PAGINA.get(p["url"])
    boton = T.boton(cta[0], cta[1], "", "flecha-diagonal", ' data-zona="cabecera_pagina"') if cta else T.btn_foto("", "cabecera_pagina")
    acciones = "" if t in ("contacto", "legal") else f'<div class="acciones">{boton}{T.tel("cab-int__tel", "cabecera_pagina", "o llame al " + N["telefono"])}</div>'
    if foto_cab:
        return f"""<section class="cab-int cab-int--foto">
 {foto(foto_cab, "100vw", "cab-int__img", True)}
 <div class="c cab-int__in">
  <p class="cab-int__et">{esc(p['etiqueta'])}</p>
  <h1 class="h1-int">{esc(p['h1'])}</h1>
  <p class="cab-int__corta">{inline(p['entrada_corta'])}</p>
  {acciones}
 </div>
</section>
"""
    return f"""<section class="cab-int cab-int--blanca">
 <div class="reticula" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
 <div class="c cab-int__in">
  <p class="cab-int__et">{esc(p['etiqueta'])}</p>
  <h1 class="h1-int">{esc(p['h1'])}</h1>
  <p class="cab-int__corta">{inline(p['entrada_corta'])}</p>
  {acciones}
 </div>
</section>
"""


def intro_int(p, intro, foto_der):
    ps = [c for t, c in intro if t == "p" and not R_FOTO.match(c)]
    if not ps:
        return ""
    temas = TEMAS.get(p["url"], [])
    pil = f'<ul class="temas">{"".join(f"<li>{esc(x)}</li>" for x in temas)}</ul>' if temas else ""
    der = f'<div class="intro__der rv">{foto(foto_der, "(max-width: 900px) 100vw, 60vw")}</div>' if foto_der else ""
    return f"""<section class="intro{' intro--sola' if not foto_der else ''}">
 <div class="c intro__in">
  <div class="intro__izq rv">
   {"".join(f'<p class="intro__p">{inline(x)}</p>' for x in ps)}
   {pil}
  </div>
  {der}
 </div>
</section>
"""


def seccion_int(s, oscura=False, form=""):
    cuerpo = render(s["bl"])
    # las reseñas y el mapa salen a todo el ancho, debajo de la sección
    fuera = []
    for m in re.finditer(r'<figure class="opinion rv ">.*?</figure>|<div class="mapa rv">.*?</div>', cuerpo, re.S):
        fuera.append(m.group(0))
    for f in fuera:
        cuerpo = cuerpo.replace(f, "")
    sec = f"""<section class="sec{' sec--oscura' if oscura else ''}" id="{slug(s['h2'])}">
 <div class="c sec__in">
  <h2 class="h2 sec__h2 rv">{h2_clave(s['h2'])}</h2>
  <div class="sec__cuerpo prosa">{cuerpo}{form}</div>
 </div>
</section>
"""
    if fuera:
        sec += f'<section class="sec-ancha"><div class="c">{"".join(fuera)}</div></section>\n'
    return sec


def formulario(tipo, url):
    """Presupuesto por foto (contacto, opción B) o candidatura (trabaja con nosotros). Lo procesa enviar.php."""
    priv = f'<p class="form__priv">{esc(texto("form_privacidad")) if tipo == "presupuesto" else "SOLVENTO INSTALACIONES Y MANTENIMIENTO, S.L. usará sus datos solo para valorar su candidatura (art. 6.1.b del RGPD)."} Sus derechos, en la <a href="/privacidad/">política de privacidad</a>.</p>'
    comun = f"""<input type="hidden" name="tipo" value="{tipo}"><input type="hidden" name="pagina" value="{url}"><input type="hidden" name="t" value="">
  <label class="trampa" aria-hidden="true">Web<input type="text" name="web" tabindex="-1" autocomplete="off"></label>"""
    if tipo == "presupuesto":
        quien = "".join(f'<label class="opcion"><input type="radio" name="quien" value="{v}"{" checked" if k == 0 else ""}><span>{esc(t)}</span></label>'
                        for k, (v, t) in enumerate(QUIEN))
        campos = f"""<fieldset class="form__quien"><legend>¿Quién nos escribe?</legend>{quien}</fieldset>
  <div class="form__fila"><label>Nombre<input type="text" name="nombre" autocomplete="name" required maxlength="80"></label>
  <label>Teléfono<input type="tel" name="telefono" autocomplete="tel" inputmode="tel" required pattern="[0-9 +()\\-]{{9,20}}" maxlength="20"></label></div>
  <div class="form__fila"><label><span>Correo <span class="opcional">(opcional)</span></span><input type="email" name="correo" autocomplete="email" maxlength="120"></label>
  <label data-solo="administrador"><span>Administración o comunidad <span class="opcional">(opcional)</span></span><input type="text" name="comunidad" maxlength="120"></label></div>
  <label><span><span data-etq="administrador">Dirección del edificio</span><span data-etq="particular" hidden>Municipio</span></span><input type="text" name="donde" required maxlength="160" placeholder="Calle y municipio"></label>
  <label>Qué necesita<select name="necesita" required><option value="">Elija una opción</option><option>Bajante de amianto</option><option>Fuga o fontanería</option><option>Generales de agua o saneamiento</option><option>Cubierta, terraza o filtración</option><option>Trabajo en altura (canalón, bajante por fuera)</option><option>Gas o calefacción</option><option>Caldera, termo o calentador</option><option>Aire acondicionado</option><option>Otro</option></select></label>
  <label><span>Qué pasa <span class="opcional">(opcional)</span></span><textarea name="mensaje" maxlength="2000" placeholder="Dónde está, desde cuándo y lo que vea en la foto"></textarea></label>
  <label class="form__foto"><span>Foto <span class="opcional">(opcional, pero nos ayuda mucho; hasta 3, {FOTO_MAX_MB} MB cada una)</span></span><input type="file" name="foto[]" accept="image/*" multiple data-max="{FOTO_MAX_MB}"><span class="form__foto-txt" data-foto-txt>{T.ico("camara")}Haga o elija una foto de la bajante o de la avería</span></label>"""
        boton = "Enviar y recibir presupuesto"
    else:
        campos = f"""<div class="form__fila"><label>Nombre<input type="text" name="nombre" autocomplete="name" required maxlength="80"></label>
  <label>Teléfono<input type="tel" name="telefono" autocomplete="tel" inputmode="tel" required pattern="[0-9 +()\\-]{{9,20}}" maxlength="20"></label></div>
  <div class="form__fila"><label>Oficio<select name="oficio" required><option value="">Elija</option><option>Albañil</option><option>Fontanero</option><option>Otro</option></select></label>
  <label>Años de experiencia<input type="text" name="anios" inputmode="numeric" maxlength="20"></label></div>
  <label>Municipio donde vive<input type="text" name="donde" autocomplete="address-level2" maxlength="80"></label>
  <label>Cuéntenos en dos líneas dónde ha trabajado<textarea name="mensaje" maxlength="1500"></textarea></label>
  <label class="form__foto"><span>Currículum <span class="opcional">(opcional; PDF, Word o foto, hasta {FOTO_MAX_MB} MB)</span></span><input type="file" name="foto[]" accept=".pdf,.doc,.docx,image/*" data-max="{FOTO_MAX_MB}"><span class="form__foto-txt" data-foto-txt>{T.ico("documento")}Adjunte su currículum si lo tiene</span></label>"""
        boton = "Enviar candidatura"
    return f"""<form class="form rv" id="presupuesto" action="/enviar.php" method="post" enctype="multipart/form-data" data-form="{tipo}">
  <div class="aviso aviso--ok" id="form-ok" hidden>{texto("form_ok") if tipo == "presupuesto" else "Recibido. Le llamamos para conocerle, de lunes a viernes."}</div>
  <div class="aviso aviso--error" id="form-error" hidden>No se ha podido enviar. Llámenos al {N['telefono']} o inténtelo de nuevo.</div>
  {comun}
  {campos}
  {priv}
  <div class="acciones"><button class="btn" type="submit"><span>{boton}</span>{T.ico("flecha-diagonal", "btn__ico")}</button></div>
</form>"""


def contacto_cuerpo(p, intro):
    ps = [c for t, c in intro if t == "p" and not R_FOTO.match(c)]
    return f"""<section class="contacto">
 <div class="c contacto__in">
  <div class="contacto__datos">
   {f'<div class="prosa rv">{"".join(f"<p>{inline(x)}</p>" for x in ps)}</div>' if ps else ""}
   <p class="contacto__et">Llámenos</p>
   {T.tel("contacto__tel", "contacto")}
   {T.estado()}
   <address class="contacto__dir">
    <p>Oficina: <a class="tel" href="tel:{N['oficina_e164']}">{N['oficina']}</a> · <a href="mailto:{N['email']}">{N['email']}</a></p>
    <p>{N['horario_texto']}.</p>
    <p><a href="{FICHA}" rel="noopener" target="_blank">{N['calle']}, {N['zona_calle']}, {N['cp']} {N['localidad']}</a></p>
   </address>
  </div>
  <div class="contacto__form">{formulario("presupuesto", p["url"])}</div>
 </div>
</section>
"""


# ---------- Página ----------
def pagina(p):
    t = datos.tipo_de(p["url"])
    intro, secs = secciones(p["bloques"])
    cuerpo = []
    USADAS.clear()
    if t == "home":
        cuerpo.append(portada_home(p))
        cuerpo.append(cinta_html())
        dec = [c for tt, c in intro if tt == "p" and not R_FOTO.match(c)]
        cuerpo.append(estrella(dec))
        op = None
        for s in secs:
            pieza = next((v for k, v in PIEZAS_H2.items() if s["h2"].startswith(k)), None)
            for tt, c in s["bl"]:
                if tt == "p" and R_OPINION.match(c):
                    op = op or R_OPINION.match(c).group(1)
                    fr = R_FRAG.search(c)
                    if fr:
                        FRAG[int(R_OPINION.match(c).group(1))] = fr.group(1)
            if pieza == "filas":
                cuerpo.append(filas_serv(s))
                cuerpo.append("<!--OPINION-->")
                ult = [c for tt, c in s["bl"] if tt == "p" and not R_FOTO.match(c) and not plano(c).endswith(":")]
                cuerpo.append(propia(ult[-1] if len(ult) > 1 else ""))
            elif pieza == "papeles":
                cuerpo.append(papeles(s))
            elif isinstance(pieza, tuple) and pieza[0] == "puntos":
                cuerpo.append(puntos(s, pieza[1], pieza[2]))
            elif isinstance(pieza, tuple) and pieza[0] == "zona":
                cuerpo.append(zona(s, pieza[1], pieza[2]))
            else:
                cuerpo.append(seccion_int(s))
        html_c = "".join(cuerpo).replace("<!--OPINION-->", opinion_y_cifras(op) if op else "")
        cuerpo = [html_c, faq_html(p["faq"])]
    else:
        todas = fotos_de(intro) + [f for s in secs for f in fotos_de(s["bl"])]
        foto_cab = next((f for f in todas if ancha(f)), None) if t != "contacto" else None
        if foto_cab:
            USADAS.add(foto_cab)
        cuerpo.append(cab_int(p, t, foto_cab))
        cuerpo.append(migas_html(p["url"]))
        if t == "contacto":
            cuerpo.append(intro_int(p, intro, None))
            antes = [s for s in secs if s["h2"].startswith("¿Cómo pido")]
            for s in antes:
                cuerpo.append(seccion_int(s))
            cuerpo.append(contacto_cuerpo(p, []))
            for s in secs:
                if s in antes or s["h2"].startswith("¿Quién nos escribe"):
                    continue
                cuerpo.append(seccion_int(s))
        else:
            # la segunda foto de la entrada (si hay) va a la derecha de la entrada; la primera ya está en la cabecera
            resto_intro = [f for f in fotos_de(intro) if f not in USADAS]
            if resto_intro:
                USADAS.add(resto_intro[0])
            cuerpo.append(intro_int(p, intro, resto_intro[0] if resto_intro else None))
            for k, s in enumerate(secs):
                form = formulario("empleo", p["url"]) if (p["url"] == "/trabaja-con-nosotros/" and any(tt == "p" and c.startswith("**Formulario:**") for tt, c in s["bl"])) else ""
                cuerpo.append(seccion_int(s, oscura=(k == 1 and len(secs) > 2 and not form), form=form))
        cuerpo.append(faq_html(p["faq"], enlace=p["url"] != URLS["faq"]))
    robots = "noindex, follow" if (t == "contacto" and not CONTACTO_INDEXABLE) else "index, follow"
    pre = None
    if t == "home" and PORTADA_FOTO:
        b = PORTADA_FOTO.rsplit(".", 1)[0]
        pre = (f"/img/{b}-800.webp 800w, /img/{b}-1600.webp 1600w", "(max-width: 1240px) 100vw, 1200px")
    return montar(T.cabeza(p, schema_de(p), robots, pre) + T.cabecera(p["url"]) + "".join(cuerpo) + T.pie(p["url"]))


def montar(h):
    return h.replace("<!--SPRITE-->", T.sprite(h), 1)


# ---------- Legales y 404 ----------
def legales():
    txt = open(os.path.join(RAIZ, "contenido", "legales", "legales.md"), encoding="utf-8").read()
    res = []
    for m in re.finditer(r"^## (/[^\n]+/)\n(.*?)(?=^## /|\Z)", txt, re.S | re.M):
        url, cuerpo = m.group(1).strip(), m.group(2).strip()
        lineas = cuerpo.split("\n")
        res.append((url, lineas[0].strip(), "\n".join(lineas[1:]).strip().replace("\n---", "")))
    return res


def pagina_legal(url, titulo, md):
    p = {"url": url, "title": f"{titulo} | {N['nombre']}", "meta": f"{titulo} de solvento.es.", "h1": titulo,
         "etiqueta": "Información legal", "entrada_corta": N["razon_social"] + " · CIF " + N["cif"]}
    NOMBRE_CORTO[url] = titulo
    bl = []
    for par in re.split(r"\n\s*\n", md):
        par = par.strip()
        if not par:
            continue
        bl.append(("h2l", par) if (len(par) < 90 and not par.endswith(".") and "\n" not in par and not par.startswith("Política de privacidad de Google")) else ("p", par))
    htmlc = "".join(f'<h2 class="h2-legal">{esc(c)}</h2>' if t == "h2l" else
                    "".join(f"<p>{inline(x)}</p>" for x in c.split("\n") if x.strip()) for t, c in bl)
    schema = {"@context": "https://schema.org", "@graph": [negocio_schema(), {"@type": "WebPage", "url": DOMINIO + url, "name": titulo,
                                                                          "dateModified": fecha_mod(os.path.join(RAIZ, "contenido", "legales", "legales.md"))}]}
    return montar(T.cabeza(p, schema, "noindex, follow") + T.cabecera(url) + cab_int(p, "legal", None) + migas_html(url)
                  + f'<section class="sec sec--legal"><div class="c"><div class="prosa legal">{htmlc}</div></div></section>' + T.pie())


def pagina_404():
    p = {"url": "/404/", "title": f"Página no encontrada | {N['nombre']}", "meta": "Esta página no existe.", "h1": "Esta página no existe",
         "etiqueta": "Error 404", "entrada_corta": texto("error_texto")}
    schema = {"@context": "https://schema.org", "@graph": [negocio_schema()]}
    return montar(T.cabeza(p, schema, "noindex, follow") + T.cabecera("") + cab_int(p, "404", None) + T.pie())


def fecha_mod(ruta):
    import datetime, subprocess
    hoy = datetime.date.today().isoformat()
    try:
        r = subprocess.run(["git", "status", "--porcelain", "--", ruta], cwd=RAIZ, capture_output=True, text=True, timeout=20)
        if r.returncode == 0:
            if r.stdout.strip():
                return hoy
            f = subprocess.run(["git", "log", "-1", "--format=%cs", "--", ruta], cwd=RAIZ, capture_output=True, text=True, timeout=20).stdout.strip()
            if f:
                return f
    except Exception:
        pass
    try:
        return datetime.date.fromtimestamp(os.path.getmtime(ruta)).isoformat()
    except OSError:
        return hoy


def escribir(url, contenido):
    ruta = os.path.join(SITIO, url.strip("/"), "index.html") if url != "/" else os.path.join(SITIO, "index.html")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    open(ruta, "w", encoding="utf-8").write(contenido)


def main():
    if os.path.isdir(SITIO):
        shutil.rmtree(SITIO)
    os.makedirs(SITIO)
    urls = []
    for p in PAGINAS:
        p["mod"] = fecha_mod(p["ruta"])
        escribir(p["url"], pagina(p))
        if CONTACTO_INDEXABLE or datos.tipo_de(p["url"]) != "contacto":
            urls.append((p["url"], p["mod"]))
    for url, tit, md in legales():
        escribir(url, pagina_legal(url, tit, md))
    open(os.path.join(SITIO, "404.html"), "w", encoding="utf-8").write(pagina_404())
    sm = "".join(f"<url><loc>{DOMINIO}{u}</loc><lastmod>{f}</lastmod></url>" for u, f in urls)
    open(os.path.join(SITIO, "sitemap.xml"), "w", encoding="utf-8").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    open(os.path.join(SITIO, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\nDisallow: /enviar.php\n\nSitemap: {DOMINIO}/sitemap.xml\n")
    llms = [texto("llms_titulo"), "",
            f"> {texto('llms_resumen')} {N['horario_texto']}. Teléfono {N['telefono']}.", "",
            "## Datos del negocio",
            f"- Nombre: {N['nombre']} ({N['razon_social']}, CIF {N['cif']}).",
            f"- Dirección: {N['calle']}, {N['zona_calle']}, {N['cp']} {N['localidad']} ({N['provincia']}).",
            f"- Teléfono: {N['telefono']} · Oficina: {N['oficina']} · Correo: {N['email']} · Ficha de Google: {FICHA}",
            f"- Horario: {N['horario_texto']}.",
            *TEXTOS["llms_datos"], "", f"## Lo que {N['nombre']} no hace", *TEXTOS["llms_no_hace"], "", "## Páginas principales"]
    llms += [f"- [{nombre(u)}]({DOMINIO}{u}): {POR_URL[u]['meta']}" for u in LLMS_PRINCIPALES if u in POR_URL]
    llms += ["", "## Municipios"] + [f"- [{v}]({DOMINIO}{k})" for k, v in PUEBLO.items() if k in POR_URL]
    open(os.path.join(SITIO, "llms.txt"), "w", encoding="utf-8").write("\n".join(llms) + "\n")
    json.dump(sorted(PENDIENTES), open(os.path.join(SITIO, "..", "generador", "_fotos_pendientes.json"), "w"), ensure_ascii=False)
    print(f"build: {len(PAGINAS)} páginas + {len(legales())} legales + 404 · sitemap con {len(urls)} URLs")


if __name__ == "__main__":
    main()

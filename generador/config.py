# -*- coding: utf-8 -*-
"""GYF-Archidex · CONFIGURACIÓN DEL CLIENTE (Solvento). Es el único archivo de Python que se toca para una web nueva.

Regla: ante cualquier discrepancia de datos manda la ficha de Google Business Profile
(00-AUDITORIAS-DE-PARTIDA/FICHA-GOOGLE-29-09-2026.md). Nada inventado: lo que no consta, no se escribe.
Firma gráfica: 07-FIRMA-GRAFICA/FIRMA.md (opciones de 007-ARCHIDEX/VARIACIONES.md).
"""

VERSION = "1"          # sube en cada entrega: estilo.css?v=VERSION y main.js?v=VERSION

# ---------- Sitio ----------
DOMINIO = "https://solvento.es"                         # sin www (Álvaro, 29/09)
HOST_PRODUCCION = ("solvento.es", "www.solvento.es")    # GTM y cookies solo cargan aquí
GTM_ID = ""                                             # sin contenedor heredado (solo un UA muerto): se crea en el paso 24
COOKIES_CLAVE = "solvento-cookies"
COLOR_TEMA = "#FFFFFF"
CONTACTO_INDEXABLE = True

# ---------- Negocio (de la ficha de Google) ----------
NEGOCIO = {
    "nombre": "Solvento",
    "nombre_largo": "Solvento · Mantenimiento de edificios",
    "razon_social": "SOLVENTO INSTALACIONES Y MANTENIMIENTO, S.L.",
    "cif": "B88551635",
    "telefono": "910 06 70 60",
    "telefono_e164": "+34910067060",
    "oficina": "696 87 86 93",
    "oficina_e164": "+34696878693",
    "email": "info@solvento.es",
    "calle": "C/ de la Electricidad, 10",
    "zona_calle": "Polígono San José de Valderas",
    "cp": "28918",
    "localidad": "Leganés",
    "provincia": "Madrid",
    "region": "Comunidad de Madrid",
    "horario_texto": "De lunes a viernes, de 9:00 a 14:00 y de 16:00 a 18:00",
    "horario_corto": "L-V · 9-14 y 16-18",
    "dias_texto": "Lunes a viernes",
    "tramos": [("09:00", "14:00"), ("16:00", "18:00")],
    "dias_schema": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "zona_horaria": "Europe/Madrid",
    # Fiestas nacionales y de la Comunidad de Madrid (día/mes) + Jueves y Viernes Santo (días desde Pascua)
    "festivos": ["1/1", "6/1", "1/5", "2/5", "15/8", "12/10", "1/11", "6/12", "8/12", "25/12"],
    "festivos_pascua": [-3, -2],
    "cid": "7789667702512089212",
    "lat": 40.3487739, "lng": -3.8012397,
    "schema_tipo": "Plumber",                       # Matías (planos locales): el de la categoría principal de la ficha
    "servicio_tipo": "Mantenimiento de instalaciones de edificios",
    "rera": "2800625",
    "knows_about": ["Sustitución de bajantes de amianto", "Fontanería de comunidades de vecinos",
                    "Impermeabilización de cubiertas", "Trabajos verticales", "Instalaciones de gas",
                    "Salas de calderas", "Calderas", "Aire acondicionado"],
}

FUENTES_PRECARGA = ["bai-jamjuree-500.woff2"]

# ---------- Marca (recursos/marca/) ----------
MARCA = {
    "logo": "solvento-logotipo-color.svg", "logo_ancho": 650, "logo_alto": 236,
    "logo_blanco": "solvento-logotipo-blanco.svg",
    "logo_trazo": "solvento-logotipo-trazo.svg",
    "gota": "solvento-gota-color.svg",
    "gota_blanca": "solvento-gota-blanco.svg",
    "gota_turquesa": "solvento-gota-turquesa.svg",
    "og": "og-solvento.jpg",
}

# ---------- URLs ----------
URLS = {"municipio": "/bajantes-amianto-", "empresa": "/empresa/", "contacto": "/contacto/",
        "faq": "/preguntas-frecuentes/", "admin": "/administradores-de-fincas/", "amianto": "/retirada-amianto/"}
MUNICIPIOS = [("/bajantes-amianto-alcorcon/", "Alcorcón"), ("/bajantes-amianto-leganes/", "Leganés")]

MENU = [
    ("Amianto", "/retirada-amianto/"),
    ("Comunidades", [
        ("Bajantes de amianto", "/retirada-amianto/"),
        ("Fontanería del edificio", "/fontaneria-comunidades/"),
        ("Cubiertas y terrazas", "/impermeabilizacion-cubiertas/"),
        ("Trabajos verticales", "/trabajos-verticales/"),
        ("Gas y calefacción", "/gas-calefaccion-comunidades/"),
        ("Preguntas frecuentes", "/preguntas-frecuentes/"),
    ]),
    ("Administradores", "/administradores-de-fincas/"),
    ("Particulares", [
        ("Fontanería en casa", "/particulares/"),
        ("Calderas", "/calderas/"),
        ("Aire acondicionado", "/aire-acondicionado/"),
    ]),
    ("Empresa", "/empresa/"),
    ("Contacto", "/contacto/"),
]

NOMBRE_CORTO = {
    "/": "Inicio",
    "/retirada-amianto/": "Bajantes de amianto",
    "/administradores-de-fincas/": "Administradores de fincas",
    "/fontaneria-comunidades/": "Fontanería del edificio",
    "/impermeabilizacion-cubiertas/": "Cubiertas y terrazas",
    "/trabajos-verticales/": "Trabajos verticales",
    "/gas-calefaccion-comunidades/": "Gas y calefacción",
    "/preguntas-frecuentes/": "Preguntas frecuentes",
    "/particulares/": "Particulares",
    "/calderas/": "Calderas",
    "/aire-acondicionado/": "Aire acondicionado",
    "/bajantes-amianto-alcorcon/": "Bajantes de amianto en Alcorcón",
    "/bajantes-amianto-leganes/": "Bajantes de amianto en Leganés",
    "/empresa/": "Empresa",
    "/contacto/": "Contacto",
    "/trabaja-con-nosotros/": "Trabaja con nosotros",
}
# Migas: página madre de cada interior (si no cuelga de la portada)
MADRE = {u: "/administradores-de-fincas/" for u in ("/retirada-amianto/", "/fontaneria-comunidades/",
         "/impermeabilizacion-cubiertas/", "/trabajos-verticales/", "/gas-calefaccion-comunidades/")}
MADRE.update({"/calderas/": "/particulares/", "/aire-acondicionado/": "/particulares/",
              "/bajantes-amianto-alcorcon/": "/retirada-amianto/", "/bajantes-amianto-leganes/": "/retirada-amianto/"})

# ---------- Portada (firma §2) ----------
# Sellos de la banda de marca (opción A con la foto cambiada por la banda): valor, texto
SELLOS = [("2800625", "Inscritos en el RERA, con plan de trabajo general aprobado"),
          ("1,3 M€", "Seguro de responsabilidad civil con MAPFRE"),
          ("1-2 días", "de obra para cambiar una bajante, en la mayoría de los casos")]
# Foto de la portada: excepción al paso 16 decidida por Álvaro el 03/10/2026 (foto de Gemini).
PORTADA_FOTO = "limpieza-canalones-trabajos-verticales.jpg"
SELLOS_NOTA = "Amianto · RERA n.º 2800625"
# Sección del trabajo estrella (hueco de project-6): frase grande (sale del texto de la portada) + 3 tarjetas
ESTRELLA_FRASE = "Lo que se rompe en una comunidad casi nunca está a la vista."
ESTRELLA_CLAVE = "casi nunca está a la vista"
ESTRELLA_BOTON = ("Bajantes de amianto", "/retirada-amianto/")
ESTRELLA_TARJETAS = [
    ("Antes", "La bajante de uralita, tras el alicatado", "bajante-fibrocemento-antes-sustitucion.jpg",
     "Bajante de fibrocemento gris vista a través de un registro abierto en la pared alicatada de una cocina"),
    ("La obra", "Bajante nueva, en uno o dos días", "sustitucion-bajante-amianto-comunidad-leganes.jpg",
     "Bajante nueva sujeta con abrazaderas en un patio de luces visto desde abajo"),
    ("Después", "Alicatado y pintado por la misma gente", "bajante-amianto-despues-alicatado.jpg",
     "Pared de cocina con azulejos blancos recién colocados y la pared de encima recién pintada"),
]
# Filas de servicio (service-6, opción A): por URL, la foto en estadio y la palabra clave del título
FILAS_FOTO = {
    "/retirada-amianto/": ("bajante-amianto-leganes-antes.jpg", "amianto"),
    "/fontaneria-comunidades/": ("cambio-generales-agua-edificio-leganes.jpg", "edificio"),
    "/impermeabilizacion-cubiertas/": ("impermeabilizacion-cubierta-comunitaria-alcorcon.jpg", "terrazas"),
    "/trabajos-verticales/": ("trabajos-verticales-bajante-comunidad-leganes.jpg", "sin andamio"),
    "/gas-calefaccion-comunidades/": ("sala-calderas-comunitaria-leganes.jpg", "calefacción"),
}
# Plantilla propia (hueco de about-6)
PROPIA = {"frase": "No queda un agujero esperando a otro gremio.", "clave": "esperando a otro gremio.",
          "grande": ("albanileria-tras-averia-comunidad-alcorcon.jpg", "Manos con guantes extendiendo cemento cola con una llana dentada junto a azulejos nuevos"),
          "pequena": ("reposicion-azulejos-bajante-amianto.jpg", "Muestras de azulejos blancos sobre una mesa de madera, junto a una llana dentada")}
# Cifras reales, sin contador (opción B): valor, texto
CIFRAS = [("2800625", "N.º en el RERA de la Comunidad de Madrid"),
          ("1,3 M€", "Responsabilidad civil con MAPFRE"),
          ("4", "Habilitaciones certificadas por Industria")]
CIFRAS_TITULO = ("Lo que puede comprobar", "comprobar")
# Iconos de la lista de papeles (por orden de aparición en el texto)
PAPELES_ICONOS = ["documento", "certificado", "escudo", "gas", "clima", "rayo"]
# Foto de cada sección que el tema convierte en «puntos» (work-6) o en «zona» (blog-6), por el principio del H2
PIEZAS_H2 = {
    "¿Qué hacemos en su edificio": "filas",
    "¿Por qué el lunes": ("puntos", "averia-fin-de-semana-lunes-sin-recargo.jpg", "Persiana metálica de una nave a medio subir, con la luz de la mañana entrando sobre el suelo"),
    "¿Qué tiene el administrador": "papeles",
    "¿Dónde trabajamos": ("zona", "bajantes-amianto-alcorcon-furgoneta.jpg", "Furgoneta blanca aparcada delante del portal de un bloque de viviendas de ladrillo"),
}
# Píldoras de «qué incluye» bajo la entrada de cada interior
TEMAS = {
    "/retirada-amianto/": ["Retirada del amianto", "Bajante nueva", "Alicatado", "Pintura", "Certificado de residuos"],
    "/fontaneria-comunidades/": ["Generales de agua", "Montantes", "Colectores", "Arquetas", "Desatascos"],
    "/impermeabilizacion-cubiertas/": ["Cubiertas", "Terrazas", "Techo del garaje", "Sumideros"],
    "/trabajos-verticales/": ["Bajantes por fuera", "Canalones", "Limpieza de cubiertas", "Sin andamio"],
    "/gas-calefaccion-comunidades/": ["Instalaciones de gas", "Salas de calderas", "Radiadores"],
    "/administradores-de-fincas/": ["Amianto", "Fontanería", "Cubiertas", "Altura", "Gas", "Un solo proveedor"],
    "/bajantes-amianto-alcorcon/": ["RERA 2800625", "Bajante nueva", "Alicatado y pintura"],
    "/bajantes-amianto-leganes/": ["RERA 2800625", "Bajante nueva", "Alicatado y pintura"],
    "/particulares/": ["Fugas", "Presupuesto firmado", "Alcorcón y Leganés"],
    "/calderas/": ["Instalación de calderas", "Empresa habilitada en gas"],
    "/aire-acondicionado/": ["Instalación", "Empresa habilitada en climatización"],
}

# ---------- Formulario de presupuesto por foto (contacto) ----------
FOTO_MAX_MB = 8
QUIEN = [("administrador", "Soy administrador de fincas o escribo por una comunidad"), ("particular", "Soy particular")]

# Firma de la agencia en el pie
CREDITO = ("El Gordo y el Flaco", "https://elgordoyelflaco.es/")
LEGALES = [("Aviso legal", "/aviso-legal/"), ("Privacidad", "/privacidad/"), ("Cookies", "/cookies/")]

# ---------- Textos del tema ----------
TEXTOS = {
    "logo_alt": "Solvento · Mantenimiento de edificios",
    "boton": "Envíenos una foto",
    "boton_corto": "Enviar una foto",
    "cab_horario": "L-V 9-14 y 16-18",
    "opinion_fuente": "Opinión publicada en Google",
    "opiniones_fantasma": "Opiniones",
    "faq_etiqueta": "Preguntas",
    "faq_tarjeta": "¿Le queda alguna duda? Pregúntenos.",
    "faq_enlace": ("Todas las preguntas sobre el amianto", "/preguntas-frecuentes/"),
    "pie_frase": "Mándenos una foto del problema.",
    "pie_horario": "Lunes a viernes · 9-14 y 16-18",
    "estado_abierto": "Ahora atendemos · hasta las {cierra}",
    "estado_fuera": "Ahora no atendemos · déjenos un mensaje",
    "form_ok": "Recibido. Le contestamos {horario_min}, a menudo el mismo día.",
    "form_privacidad": "SOLVENTO INSTALACIONES Y MANTENIMIENTO, S.L. usará sus datos solo para responder a su solicitud y preparar el presupuesto que nos pide (art. 6.1.b del RGPD).",
    "error_texto": "Puede que el enlace esté mal o que la página haya cambiado de sitio. Llámenos y lo vemos.",
    "cookies": "Usamos cookies de Google Analytics para saber cuántas personas visitan la web. Solo se activan si las acepta.",
    "llms_titulo": "# Solvento · Mantenimiento de edificios en el sur de Madrid",
    "llms_resumen": "Empresa de mantenimiento de las instalaciones de edificios con nave en Leganés, para administradores de fincas y comunidades de vecinos. Especialidad: sustitución de bajantes de amianto (RERA n.º 2800625).",
    "llms_datos": ["- RERA n.º 2800625 y plan de trabajo general aprobado para el amianto.",
                   "- Seguro de responsabilidad civil de 1,3 millones de euros con MAPFRE.",
                   "- Habilitaciones certificadas por Industria: gas, climatización (instaladora y mantenedora), baja tensión y RITE.",
                   "- Presupuesto con una foto, a menudo el mismo día."],
    "llms_no_hace": ["- No hace urgencias: la avería del fin de semana se atiende el lunes, sin recargo.",
                     "- No hace toma de muestras de amianto ni retira depósitos, canalones o chimeneas de fibrocemento: solo sustituye bajantes."],
}
LLMS_PRINCIPALES = ["/", "/retirada-amianto/", "/administradores-de-fincas/", "/preguntas-frecuentes/", "/empresa/", "/contacto/"]


def texto(clave, **extra):
    N = NEGOCIO
    v = dict(nombre=N["nombre"], localidad=N["localidad"], telefono=N["telefono"], horario=N["horario_texto"],
             horario_min=N["horario_texto"][0].lower() + N["horario_texto"][1:], cierra="{cierra}")
    v.update(extra)
    t = TEXTOS[clave]
    return t.format(**v) if isinstance(t, str) else t


# Reseñas: contenido/resenas.json (las 61 literales de la ficha)
import json as _json, os as _os
_R = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "contenido", "resenas.json"), encoding="utf-8"))
NEGOCIO["valoracion"] = _R["valoracion"]
NEGOCIO["resenas"] = str(_R["resenas"])
RESENAS = {o["n"]: o for o in _R["todas"]}
FICHA = f"https://maps.google.com/?cid={NEGOCIO['cid']}"


# Frase grande del pie por página (si la URL no está, va TEXTOS["pie_frase"]).
PIE_FRASES = {
    "/": "Mándenos una foto de la bajante.",
    "/retirada-amianto/": "Mándenos una foto de la bajante.",
    "/bajantes-amianto-alcorcon/": "Mándenos una foto de la bajante.",
    "/bajantes-amianto-leganes/": "Mándenos una foto de la bajante.",
    "/administradores-de-fincas/": "Mándenos una foto de la bajante.",
    "/fontaneria-comunidades/": "Mándenos una foto de la avería.",
    "/impermeabilizacion-cubiertas/": "Mándenos una foto de la cubierta.",
    "/trabajos-verticales/": "Mándenos una foto de la fachada.",
    "/gas-calefaccion-comunidades/": "Mándenos una foto de la sala de calderas.",
    "/particulares/": "Mándenos una foto de la avería.",
    "/calderas/": "Mándenos una foto de la caldera.",
    "/aire-acondicionado/": "Mándenos una foto del aparato.",
    "/trabaja-con-nosotros/": "Buscamos oficiales con oficio.",
}

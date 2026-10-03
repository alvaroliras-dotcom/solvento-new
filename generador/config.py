# -*- coding: utf-8 -*-
"""GYF-Rayo · CONFIGURACIÓN DEL CLIENTE: Solvento (v2, 03/10/2026).

Tema 003-RAYO de la biblioteca (el de la web de GYF), con la firma de Solvento: portada oscura con la gota en 3D,
galería de obras que sube, amianto paso a paso clavado, cifras en mosaico, formulario con fotos adjuntas.
Regla: ante cualquier discrepancia de datos manda la ficha de Google (00-AUDITORIAS-DE-PARTIDA). Nada inventado.
Marcadores en los textos: {pueblo}, {nombre}, {localidad}, {telefono}, {horario}, {horario_min}, {abre}, {cierra}.
"""

VERSION = "2"          # sube en cada entrega: estilo.css?v=VERSION y main.js?v=VERSION

# ---------- Sitio ----------
DOMINIO = "https://solvento.es"                         # sin www (Álvaro, 29/09)
HOST_PRODUCCION = ("solvento.es", "www.solvento.es")    # GTM y cookies solo cargan aquí
GTM_ID = ""                                             # se crea al publicar (paso 24)
COOKIES_CLAVE = "solvento-cookies"
COLOR_TEMA = "#0B3B3E"
REDIRECCIONES = []                                      # las 301/410 salen de generador/mapa301.json (Bruno)
REDIRECCIONES_302 = []
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
    "whatsapp": None,                                   # no consta: en su lugar va «Envíenos una foto»
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
    "abre": "09:00", "cierra": "18:00",
    "tramos": [("09:00", "14:00"), ("16:00", "18:00")],
    "dias_schema": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "zona_horaria": "Europe/Madrid",
    "festivos": ["1/1", "6/1", "1/5", "2/5", "15/8", "12/10", "1/11", "6/12", "8/12", "25/12"],
    "festivos_pascua": [-3, -2],
    "valoracion": "4,1", "resenas": "61",               # se leen de contenido/resenas.json (abajo)
    "anios": "", "anios_marca": "", "garantia": "", "fundacion": None,
    "devuelve_llamada": None,
    "cambia_equipos": None,
    "cid": "7789667702512089212",
    "lat": 40.3487739, "lng": -3.8012397,
    "schema_tipo": "Plumber",
    "servicio_tipo": "Mantenimiento de instalaciones de edificios",
    "precio": None,
    "pago": None,
    "rera": "2800625",
    "knows_about": ["Sustitución de bajantes de amianto", "Fontanería de comunidades de vecinos",
                    "Impermeabilización de cubiertas", "Trabajos verticales", "Instalaciones de gas",
                    "Salas de calderas"],
    "persona": None,
}

FUENTES_PRECARGA = ["bai-jamjuree-600.woff2", "bai-jamjuree-400.woff2", "bai-jamjuree-500.woff2"]

# ---------- Marca ----------
MARCA = {
    "simbolo": "solvento-gota-turquesa.svg",
    "logo": "solvento-logotipo-color.svg",
    "logo_ancho": 650, "logo_alto": 236,
    "logo_blanco": "solvento-logotipo-blanco.svg",
    "og": "og-solvento.jpg",
}

# ---------- Objeto de portada: la gota de Solvento en 3D ----------
OBJETO_PORTADA = {
    "tipo": "3d",
    "imagen": "gota-3d.png",
    "ancho": 840, "alto": 840,
    "alt": "",
    "video_webm": None, "video_mov": None,
    "svg_3d": "solvento-gota-turquesa.svg",
    "color_3d": "#00AFAA",
    "color_unico": True,
    "en_banda": True,
}

# ---------- URLs ----------
URLS = {
    "hub": None,
    "municipio": "/bajantes-amianto-",
    "marca": None,
    "empresa": "/empresa/",
    "contacto": "/contacto/",
    "admin": "/administradores-de-fincas/",
    "amianto": "/retirada-amianto/",
    "faq": "/preguntas-frecuentes/",
}
MUNICIPIOS = [("/bajantes-amianto-leganes/", "Leganés"), ("/bajantes-amianto-alcorcon/", "Alcorcón")]
PREFIJOS_MUNICIPIO = ["Bajantes de amianto en"]
MUNICIPIO_ANCLA = "Bajantes de amianto en {pueblo}"

# Menú a pantalla completa. Particulares fuera del menú (Álvaro, 03/10: la web es para administradores): solo en el pie.
MENU = [
    ("Inicio", "/"),
    ("Bajantes de amianto", "/retirada-amianto/"),
    ("Administradores de fincas", "/administradores-de-fincas/"),
    ("Comunidades", [
        ("Bajantes de amianto", "/retirada-amianto/"),
        ("Fontanería del edificio", "/fontaneria-comunidades/"),
        ("Cubiertas y terrazas", "/impermeabilizacion-cubiertas/"),
        ("Trabajos verticales", "/trabajos-verticales/"),
        ("Gas y calefacción", "/gas-calefaccion-comunidades/"),
        ("Preguntas sobre el amianto", "/preguntas-frecuentes/"),
    ]),
    ("Zonas", [(f"Bajantes en {n}", u) for u, n in MUNICIPIOS]),
    ("Empresa", "/empresa/"),
    ("Contacto", "/contacto/"),
]
PARTICULARES = [("Fontanería en casa", "/particulares/"), ("Calderas", "/calderas/"), ("Aire acondicionado", "/aire-acondicionado/")]

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
# Migas: madre de cada interior (si no cuelga de la portada)
MADRE = {u: "/administradores-de-fincas/" for u in ("/retirada-amianto/", "/fontaneria-comunidades/",
         "/impermeabilizacion-cubiertas/", "/trabajos-verticales/", "/gas-calefaccion-comunidades/")}
MADRE.update({"/calderas/": "/particulares/", "/aire-acondicionado/": "/particulares/",
              "/bajantes-amianto-alcorcon/": "/retirada-amianto/", "/bajantes-amianto-leganes/": "/retirada-amianto/"})

# Servicios: (título, texto corto, url, icono, etiquetas, foto). Filas con la foto que sigue al cursor (R23).
SERVICIOS_HOME = [
    ("Bajantes de amianto", "Retiramos el fibrocemento con plan aprobado, ponemos la bajante nueva, alicatamos y pintamos.",
     "/retirada-amianto/", "bajante", ["RERA 2800625", "1-2 días"], "bajante-fibrocemento-antes-sustitucion.jpg"),
    ("Fontanería del edificio", "Generales de agua, montantes, colectores, arquetas, desatascos y grupos de presión.",
     "/fontaneria-comunidades/", "herramienta", ["Generales", "Saneamiento"], "cambio-generales-agua-edificio-leganes.jpg"),
    ("Cubiertas y terrazas", "Filtraciones desde la cubierta, la terraza o el techo del garaje, y el techo del vecino repuesto.",
     "/impermeabilizacion-cubiertas/", "cubierta", ["Filtraciones", "Sumideros"], "impermeabilizacion-cubierta-comunitaria-alcorcon.jpg"),
    ("Trabajos en altura", "Bajantes por fuera, canalones y cubiertas, sin montar andamio.",
     "/trabajos-verticales/", "altura", ["Sin andamio", "Canalones"], "trabajos-verticales-bajante-comunidad-leganes.jpg"),
    ("Gas y calefacción", "Instalaciones de gas, salas de calderas comunitarias y radiadores, con habilitación de Industria.",
     "/gas-calefaccion-comunidades/", "gas", ["Gas", "RITE"], "sala-calderas-comunitaria-leganes.jpg"),
]
SERVICIOS_SECCION = True
SERVICIOS_TITULO = "¿Qué hacemos en su edificio?"
SERVICIOS_TEXTO = "Lo que se rompe en una comunidad casi nunca está a la vista: detrás del alicatado, en el techo del garaje o en la cubierta. Ahí trabajamos, con albañiles, fontaneros y pintores de la casa."

PASOS_ICONOS = []      # listas numeradas: solo el número grande (los iconos no casaban con todas las listas)
ICONO_URL = {u: ic for _, _, u, ic, _, _ in SERVICIOS_HOME}
ICONO_URL.update({"/administradores-de-fincas/": "edificio", "/preguntas-frecuentes/": "documento", "/empresa/": "escudo",
                  "/contacto/": "camara", "/trabaja-con-nosotros/": "herramienta", "/particulares/": "herramienta",
                  "/calderas/": "gas", "/aire-acondicionado/": "clima"})

# Galería que sube sobre la portada (R5): fotos de tema (Gemini) con lo que muestran; no se presentan como obras reales.
CASOS = [
    ("Bajante de fibrocemento", "antes del cambio", "bajante-amianto-alcorcon-antes.jpg", None, "v"),
    ("Patio de luces", "por donde bajan las bajantes", "patio-de-luces-comunidad-vecinos.jpg", None, "g"),
    ("Colector del garaje", "saneamiento", "colector-saneamiento-garaje-comunidad.jpg", None, "h"),
    ("Alicatado y pintura", "después de la bajante", "bajante-amianto-alcorcon-despues.jpg", None, "v"),
    ("Canalones", "sin andamio", "limpieza-canalones-trabajos-verticales.jpg", None, "h"),
    ("Sumidero de terraza", "impermeabilización", "sumidero-terraza-impermeabilizacion.jpg", None, "h"),
    ("Radiadores", "calefacción del edificio", "radiador-calefaccion-comunidad.jpg", None, "v"),
]
CASOS_VER = "Ver"

CINTA_PORTADA = ["Bajantes de amianto", "Generales de agua", "Cubiertas", "Trabajos verticales", "Gas", "RERA 2800625"]
CINTA_SECUNDARIA = ["Leganés", "Alcorcón", "Fuenlabrada", "Getafe", "Móstoles", "Madrid sur"]

# Cifras en mosaico 2 + 2: (valor, sufijo, texto, botón o None, icono). Todas de Isra o de Álvaro.
CIFRAS = [
    ("20", "", "administradores de fincas trabajan ya con nosotros, en 50 a 100 comunidades", ("Para administradores", "/administradores-de-fincas/"), "edificio"),
    ("90", " %", "de nuestras obras de amianto son para comunidades de vecinos", ("El amianto, paso a paso", "/retirada-amianto/"), "bajante"),
    ("10.000", " €", "invertidos en nuestra cabina de descontaminación", None, "escudo"),
    ("1,3", " M€", "de seguro de responsabilidad civil con MAPFRE", ("Ver los papeles", "/empresa/"), "certificado"),
]
CIFRAS_EN = {"home": 2, "empresa": 1, "servicio": 0, "municipio": 0}

# El amianto, paso a paso (sección clavada en la home y en la página del amianto): (título, texto, foto o lista de fotos:
# se usa la primera que no salga ya en la página)
AMIANTO_PASOS = [
    ("Nos cuenta qué pasa", "Por teléfono o en el formulario, con una foto de la bajante si puede: nos ayuda a hacernos una idea. A menudo le contestamos el mismo día.", "presupuesto-bajante-amianto-por-foto.jpg"),
    ("Se abre la pared", "Nuestros albañiles abren el alicatado o el tabique que tapa la bajante, en la cocina o el baño del vecino.", ["bajante-amianto-leganes-antes.jpg", "bajante-fibrocemento-antes-sustitucion.jpg", "bajante-amianto-alcorcon-antes.jpg"]),
    ("Se retira el amianto", "Con el plan de trabajo aprobado, personal formado y la cabina de descontaminación. El residuo sale embalado y etiquetado.", "residuo-amianto-etiqueta-oficial-bajante.jpg"),
    ("Bajante nueva", "Nuestros fontaneros colocan la bajante nueva. En la mayoría de los casos, la obra entera dura uno o dos días.", "sustitucion-bajante-amianto-comunidad-leganes.jpg"),
    ("Alicatado y pintura", "El vecino elige los azulejos; nosotros los compramos, los colocamos y pintamos. No queda nada para otro gremio.", ["bajante-amianto-leganes-despues.jpg", "bajante-amianto-despues-alicatado.jpg", "reposicion-azulejos-bajante-amianto.jpg"]),
    ("Certificado de residuos", "Al terminar, la comunidad recibe el certificado de residuos del amianto retirado, para su archivo.", "certificado-residuos-amianto-administrador.jpg"),
]
AMIANTO_TITULO = "El cambio de una bajante de amianto, paso a paso"
AMIANTO_ETIQUETA = "Amianto · RERA n.º 2800625"

# Secciones del texto que el tema reconoce por el principio del H2
CTA_H2 = r"^(Pide |Pida |Llámanos|Llámenos|Hablemos|Cuéntenos|¿Tiene una finca)"
CTA_ULTIMO = False
ZONA_H2 = "¿Dónde trabajamos"
HORARIO_H2 = "Horario"

CTA_EXTRA = ("Envíenos una foto", "/contacto/#presupuesto")

CREDITO = ("El Gordo y el Flaco", "https://elgordoyelflaco.es/")
LEGALES = [("Aviso legal", "/aviso-legal/"), ("Privacidad", "/privacidad/"), ("Cookies", "/cookies/")]

CONTACTO_YA = {"Teléfono", "Horario", "Email", "Correo"}
BANDA_TIT = {}

# Formulario de presupuesto por foto (contacto) y de candidatura (trabaja con nosotros)
FOTO_MAX_MB = 8
QUIEN = [("administrador", "Soy administrador de fincas o escribo por una comunidad"), ("particular", "Soy particular")]

# ---------- Textos del tema ----------
TEXTOS = {
    "oficio": "mantenimiento de edificios",
    "logo_alt": "Solvento · Mantenimiento de edificios",
    "whatsapp_saludo": "",
    "whatsapp_pueblo": "",
    "etiqueta_portada": "Comunidades de vecinos · {pueblo}",
    "corta_municipio": "{nombre} cambia bajantes de amianto en las comunidades de {pueblo}.",
    "corta": "{nombre} repara y sustituye las instalaciones de los edificios del sur de Madrid.",
    "tarjeta_titulo": "¿Le llamamos nosotros?",
    "tarjeta_ir": "Déjenos su teléfono",
    "llamada_titulo": "Déjenos su nombre y su teléfono",
    "llamada_promesa": "Le llamamos en horario de oficina.",
    "llamada_ok": "Recibido. Le llamamos {horario_min}.",
    "llamada_boton": "Que me llamen",
    "promesa_abierto": "Le llamamos en cuanto podamos.",
    "promesa_antes": "Le llamamos hoy a partir de las {abre}.",
    "promesa_siguiente": "Le llamamos {dia} a partir de las {abre}.",
    "declara_etiqueta": "Quiénes somos",
    "indice_titulo": "En esta página",
    "indice_llamar": "¿Tiene la foto?",
    "opiniones_etiqueta": "Opiniones en Google",
    "opiniones_titular": "Lo que dicen de Solvento en Google",
    "opiniones_sello": "{valoracion} EN GOOGLE · {resenas} RESEÑAS · ",
    "resenas_ficha": "Valoración media en la ficha de {nombre}",
    "faq_etiqueta": "Dudas habituales",
    "faq_titulo": "Preguntas frecuentes",
    "faq_cta": "¿No está su pregunta? Llámenos",
    "cifras_etiqueta": "{nombre} en cifras",
    "cifras_titulo": "Lo que puede comprobar",
    "cifras_fecha": "Datos de la empresa, octubre de 2026.",
    "zona_titulo": "Páginas por municipio",
    "mapa_titular": "Nuestra nave, en Leganés",
    "mapa_texto": "Polígono San José de Valderas. Para empezar no hace falta venir: cuéntenos qué pasa por teléfono o en el formulario.",
    "privacidad_llamada": "Usamos sus datos solo para llamarle.",
    "privacidad_form": "SOLVENTO INSTALACIONES Y MANTENIMIENTO, S.L. usará sus datos solo para responder a su solicitud y preparar el presupuesto que nos pide (art. 6.1.b del RGPD).",
    "form_ok": "Recibido. Le contestamos {horario_min}, a menudo el mismo día.",
    "form_confianza": "Cuéntenos qué pasa. Si adjunta una foto, nos hacemos una idea antes de verlo. A menudo le contestamos el mismo día.",
    "form_municipio_ph": "Leganés, Alcorcón…",
    "form_mensaje_label": "¿Qué pasa?",
    "form_mensaje_ph": "Dónde está, desde cuándo y lo que vea en la foto",
    "form_boton": "Enviar",
    "contacto_horario_extra": "Fuera de ese horario, déjenos un mensaje y le contestamos el siguiente día laborable.",
    "banda_etiqueta": "Presupuesto para la junta",
    "banda_titulo": "Cuéntenos qué pasa con la bajante",
    "banda_texto": "Si puede, adjunte una foto: nos ayuda a hacernos una idea. A menudo le contestamos el mismo día.",
    "estado_abierto": "Ahora atendemos · hasta las {cierra_tramo}",
    "estado_fuera": "Ahora no atendemos · déjenos un mensaje",
    "pie_titular": "Mándenos<br>una foto.",
    "error_texto": "Puede que el enlace esté mal o que la página haya cambiado de sitio. Llámenos y lo vemos.",
    "llms_titulo": "# Solvento · Mantenimiento de edificios en el sur de Madrid",
    "llms_resumen": "Empresa de mantenimiento de las instalaciones de edificios con nave en Leganés, para administradores de fincas y comunidades de vecinos. Especialidad: sustitución de bajantes de amianto (RERA n.º 2800625).",
    "llms_horario_extra": "No hace urgencias: la avería del fin de semana se atiende el lunes, sin recargo.",
    "llms_datos": ["- RERA n.º 2800625, plan de trabajo general aprobado y cabina de descontaminación propia para el amianto.",
                   "- Unos 20 administradores de fincas y entre 50 y 100 comunidades.",
                   "- Seguro de responsabilidad civil de 1,3 millones de euros con MAPFRE.",
                   "- Habilitaciones certificadas por Industria: gas, climatización (instaladora y mantenedora), baja tensión y RITE.",
                   "- Se le puede contar el problema por teléfono o en el formulario, con fotos adjuntas; a menudo contesta el mismo día."],
    "llms_no_hace": ["- No hace urgencias: la avería del fin de semana se atiende el lunes, sin recargo.",
                     "- No hace toma de muestras de amianto ni retira depósitos, canalones o chimeneas de fibrocemento: solo sustituye bajantes."],
    "llms_no_instala": "",
}
LLMS_PRINCIPALES = ["/", "/retirada-amianto/", "/administradores-de-fincas/", "/preguntas-frecuentes/", "/empresa/", "/contacto/"]
LLMS_MARCAS = []

# Pie de cada página (Merche, 03/10): (antetítulo con el problema, titular con la acción, lo que consigue[, "llamar"]).
# Regla: «Mándenos una foto» solo cuando la pregunta es un problema que se puede fotografiar; si la pregunta es
# buscar empresa, la acción es llamar (y el botón de llamar va primero).
# Si la URL no está, va PIE_DEFECTO.
_JUNTA = "Con la foto nos hacemos una idea de su edificio antes de verlo. A menudo le contestamos el mismo día."
_AVERIA = "Con la foto nos hacemos una idea de lo que pasa antes de verlo. A menudo le contestamos el mismo día."
PIE_DEFECTO = ("¿Tiene un problema en el edificio?", "Mándenos una foto.", _AVERIA)
PIE_FRASES = {
    "/": ("¿Lleva una finca con la bajante de uralita?", "Mándenos una foto.", _JUNTA),
    "/retirada-amianto/": ("¿La bajante de su edificio es de fibrocemento?", "Mándenos una foto.", _JUNTA),
    "/administradores-de-fincas/": ("¿Busca una empresa que abra, cierre y pinte, con los papeles en regla?", "Llámenos.", "Le contamos cómo trabajamos con otros 20 administradores. Y el día que tenga una avería, cuéntenosla con una foto.", "llamar"),
    "/bajantes-amianto-leganes/": ("¿Tiene una finca en Leganés con la bajante de uralita?", "Mándenos una foto.", _JUNTA),
    "/bajantes-amianto-alcorcon/": ("¿Tiene una finca en Alcorcón con la bajante de uralita?", "Mándenos una foto.", _JUNTA),
    "/preguntas-frecuentes/": ("¿Ya tiene claro que hay que cambiar la bajante?", "Mándenos una foto.", _JUNTA),
    "/fontaneria-comunidades/": ("¿Gotea en el techo del vecino de abajo?", "Mándenos una foto de la gotera.", _AVERIA),
    "/impermeabilizacion-cubiertas/": ("¿Ha salido una mancha en el techo del último piso?", "Mándenos una foto de la mancha.", "Y otra de la cubierta, si llega a ella. Nos ayuda a hacernos una idea antes de verlo."),
    "/trabajos-verticales/": ("¿Hay que llegar a una bajante o a un canalón en altura?", "Mándenos una foto desde abajo.", "Nos ayuda a ver si se llega sin andamio."),
    "/gas-calefaccion-comunidades/": ("¿Hay que tocar el gas o la sala de calderas?", "Mándenos una foto de la instalación.", "Somos empresa habilitada por Industria. Con la foto nos hacemos una idea antes de verlo."),
    "/empresa/": ("¿Busca una empresa con plantilla propia y RERA?", "Llámenos.", "Le contamos cómo trabajamos y qué papeles le damos. Sin compromiso.", "llamar"),
    "/contacto/": ("¿Prefiere hablarlo de viva voz?", "Llámenos.", "910 06 70 60, de lunes a viernes, de 9:00 a 14:00 y de 16:00 a 18:00.", "llamar"),
    "/trabaja-con-nosotros/": ("¿Es albañil o fontanero con oficio?", "Llámenos.", "O déjenos su candidatura en el formulario de esta página. Contrato indefinido y formación en amianto.", "llamar"),
    "/particulares/": ("¿Tiene una avería en casa?", "Mándenos una foto.", _AVERIA),
    "/calderas/": ("¿La caldera ya no da más de sí?", "Mándenos una foto de la caldera.", _AVERIA),
    "/aire-acondicionado/": ("¿Quiere poner o cambiar el aire acondicionado?", "Mándenos una foto de la pared.", "Donde lo quiere poner, o del aparato que quiere cambiar. Nos ayuda a hacernos una idea antes de verlo."),
}

# Banda final por página: (título, texto)
BANDA_PAGINA = {
    "/fontaneria-comunidades/": ("Cuéntenos qué avería tiene", "Si puede, adjunte una foto del cuarto de contadores, de la mancha o del atasco: nos ayuda a hacernos una idea."),
    "/impermeabilizacion-cubiertas/": ("Cuéntenos dónde está la mancha", "Si puede, adjunte fotos de la mancha y de la cubierta: nos ayudan a hacernos una idea."),
    "/trabajos-verticales/": ("Cuéntenos a qué hay que llegar", "Si puede, adjunte una foto desde abajo o desde la cubierta: nos ayuda a ver si se llega sin andamio."),
    "/gas-calefaccion-comunidades/": ("Cuéntenos qué hay que hacer en la instalación", "Si puede, adjunte una foto de la sala de calderas o de lo que haya que cambiar. Somos empresa habilitada por Industria."),
    "/empresa/": ("¿Tiene una finca con un problema?", "Cuéntenos qué pasa, con una foto si puede. A menudo le contestamos el mismo día."),
    "/trabaja-con-nosotros/": ("¿Es albañil o fontanero?", "Mándenos su candidatura desde el formulario de esta página o llámenos."),
    "/particulares/": ("Cuéntenos qué avería tiene", "Fugas, calderas, gas, termos y aire acondicionado. Si puede, adjunte una foto."),
    "/calderas/": ("Cuéntenos qué le pasa a la caldera", "Si puede, adjunte una foto: nos ayuda a hacernos una idea."),
    "/aire-acondicionado/": ("Cuéntenos qué aire quiere poner o cambiar", "Si puede, adjunte una foto de la pared o del aparato."),
}


def texto(clave, **extra):
    """Devuelve TEXTOS[clave] con los marcadores rellenos."""
    N = NEGOCIO
    v = dict(nombre=N["nombre"], localidad=N["localidad"], telefono=N["telefono"], horario=N["horario_texto"],
             horario_min=N["horario_texto"][0].lower() + N["horario_texto"][1:], anios=N["anios"],
             anios_marca=N["anios_marca"], abre=N["abre"].lstrip("0"), cierra=N["cierra"].lstrip("0"),
             garantia=N["garantia"], valoracion=N["valoracion"], resenas=N["resenas"], credencial="",
             pueblo=N["localidad"], devuelve="en cuanto podamos", cierra_tramo="{cierra_tramo}")
    v.update(extra)
    v["PUEBLO"] = v["pueblo"].upper()
    return TEXTOS[clave].format(**v)


import json as _json, os as _os
_R = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "contenido", "resenas.json"), encoding="utf-8"))
NEGOCIO["valoracion"] = _R["valoracion"]
NEGOCIO["resenas"] = str(_R["resenas"])
OPINIONES = _R.get("opiniones", [])
RESENAS = {o["n"]: o for o in _R.get("todas", [])}
FICHA = f"https://maps.google.com/?cid={NEGOCIO['cid']}"

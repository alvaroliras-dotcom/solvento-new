/* GYF-Archidex · main.js (Solvento)
   Los marcadores con doble guion bajo (__TZ__, __TRAMOS__…) los rellena generador/rematar.py con config.py.
   BASE GYF: estado abierto/cerrado (con horario partido), formularios (antispam de tiempo, recuperar lo escrito,
   avisos de vuelta), cookies con modo de consentimiento, GTM solo en producción, eventos de medición, barra fija
   del móvil y FAQ con una abierta.
   CAPA DE ARCHIDEX (firma de Solvento, movimiento bajo): cabecera con línea al bajar, desplegables del menú,
   menú del móvil, apariciones desde abajo una sola vez, formulario de presupuesto por foto (quién escribe y fotos).
   Sin librerías. Sin JS o con movimiento reducido, todo se ve quieto y completo. */
(function () {
  "use strict";
  var d = document, w = window, html = d.documentElement;
  html.classList.add("js");
  var reducido = w.matchMedia && w.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Cabecera: línea y sombra al bajar ---------- */
  var cab = d.querySelector("[data-cab]");
  function alScroll() { if (cab) cab.classList.toggle("con-sombra", w.scrollY > 8); }
  w.addEventListener("scroll", alScroll, { passive: true }); alScroll();

  /* ---------- Desplegables del menú (ratón: CSS; teclado y táctil: botón) ---------- */
  d.querySelectorAll(".nav__abre").forEach(function (b) {
    b.addEventListener("click", function () {
      var ab = b.getAttribute("aria-expanded") !== "true";
      d.querySelectorAll(".nav__abre").forEach(function (o) { o.setAttribute("aria-expanded", "false"); });
      b.setAttribute("aria-expanded", ab ? "true" : "false");
    });
  });
  d.addEventListener("click", function (e) {
    if (!e.target.closest(".nav__grupo")) d.querySelectorAll(".nav__abre").forEach(function (o) { o.setAttribute("aria-expanded", "false"); });
  });
  d.addEventListener("keydown", function (e) {
    if (e.key === "Escape") d.querySelectorAll(".nav__abre[aria-expanded=true]").forEach(function (o) { o.setAttribute("aria-expanded", "false"); o.focus(); });
  });

  /* ---------- Menú del móvil ---------- */
  var menu = d.querySelector("[data-menu]"), burger = d.querySelector(".cab__burger");
  function toggle(ab) {
    if (!menu) return;
    menu.classList.toggle("abierta", ab);
    menu.setAttribute("aria-hidden", ab ? "false" : "true");
    if (burger) burger.setAttribute("aria-expanded", ab ? "true" : "false");
    d.body.style.overflow = ab ? "hidden" : "";
    if (ab) { var c = menu.querySelector(".menu__cerrar"); if (c) setTimeout(function () { c.focus(); }, 50); } else if (burger) burger.focus();
  }
  if (burger) burger.addEventListener("click", function () { toggle(true); });
  if (menu) {
    menu.addEventListener("click", function (e) { if (e.target.closest(".menu__cerrar") || e.target.closest("a")) toggle(false); });
    d.addEventListener("keydown", function (e) {
      if (!menu.classList.contains("abierta")) return;
      if (e.key === "Escape") toggle(false);
      if (e.key === "Tab") {
        var f = menu.querySelectorAll("a[href], button"), a = f[0], z = f[f.length - 1];
        if (e.shiftKey && d.activeElement === a) { e.preventDefault(); z.focus(); }
        else if (!e.shiftKey && d.activeElement === z) { e.preventDefault(); a.focus(); }
      }
    });
  }

  /* ---------- Estado en vivo: horario partido de la ficha (config.py: tramos, dias_schema, zona_horaria) ---------- */
  var FEST = __FESTIVOS__, PASCUA = __PASCUA__, LABORABLES = __DIAS_N__, TRAMOS = __TRAMOS__;
  function pascua(y) {
    var a = y % 19, b = Math.floor(y / 100), c = y % 100, dd = Math.floor(b / 4), e = b % 4, f = Math.floor((b + 8) / 25),
      g = Math.floor((b - f + 1) / 3), h = (19 * a + b - dd - g + 15) % 30, i = Math.floor(c / 4), k = c % 4,
      l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451), mes = Math.floor((h + l - 7 * m + 114) / 31);
    return Date.UTC(y, mes - 1, ((h + l - 7 * m + 114) % 31) + 1);
  }
  function esLaborable(dt) {
    var dias = Math.round((dt.getTime() - pascua(dt.getUTCFullYear())) / 864e5);
    return LABORABLES.indexOf(dt.getUTCDay()) > -1 && PASCUA.indexOf(dias) < 0 && FEST.indexOf(dt.getUTCDate() + "/" + (dt.getUTCMonth() + 1)) < 0;
  }
  var ABIERTO = null;
  function hhmm(m) { return Math.floor(m / 60) + ":" + ("0" + (m % 60)).slice(-2); }
  function estado() {
    var p = {};
    try {
      new Intl.DateTimeFormat("en-GB", { timeZone: "__TZ__", year: "numeric", day: "numeric", month: "numeric", hour: "numeric", minute: "numeric", hour12: false })
        .formatToParts(new Date()).forEach(function (x) { p[x.type] = x.value; });
    } catch (e) { return; }
    var min = (parseInt(p.hour, 10) % 24) * 60 + parseInt(p.minute, 10);
    var hoy = new Date(Date.UTC(parseInt(p.year, 10), parseInt(p.month, 10) - 1, parseInt(p.day, 10)));
    var tramo = null;
    if (esLaborable(hoy)) TRAMOS.forEach(function (t) { if (min >= t[0] && min < t[1]) tramo = t; });
    ABIERTO = !!tramo;
    d.querySelectorAll("[data-estado]").forEach(function (el) {
      el.classList.add(tramo ? "abierto" : "fuera");
      var s = el.querySelector("span");
      if (s) s.textContent = tramo ? __ESTADO_ABIERTO__.replace("{cierra}", hhmm(tramo[1])) : __ESTADO_FUERA__;
    });
  }
  estado();
  d.querySelectorAll("[data-anio]").forEach(function (e) { e.textContent = new Date().getFullYear(); });

  /* ---------- Formulario de presupuesto: quién escribe (cambia campos y etiquetas) y las fotos elegidas ---------- */
  d.querySelectorAll("[data-form]").forEach(function (f) {
    function quien() {
      var r = f.querySelector('input[name="quien"]:checked'); if (!r) return;
      f.querySelectorAll("[data-solo]").forEach(function (el) { el.hidden = el.getAttribute("data-solo") !== r.value; });
      f.querySelectorAll("[data-etq]").forEach(function (el) { el.hidden = el.getAttribute("data-etq") !== r.value; });
    }
    f.addEventListener("change", function (e) {
      if (e.target.name === "quien") quien();
      if (e.target.type === "file") {
        var inp = e.target, max = parseFloat(inp.getAttribute("data-max") || "8") * 1048576, txt = f.querySelector("[data-foto-txt]");
        var fs = [].slice.call(inp.files || []);
        if (fs.length > 3) { alert("Puede adjuntar hasta 3 archivos."); inp.value = ""; return; }
        if (fs.some(function (x) { return x.size > max; })) { alert("Alguno de los archivos pesa demasiado. Pruebe con una foto más pequeña."); inp.value = ""; return; }
        if (txt && fs.length) { txt.lastChild.textContent = fs.map(function (x) { return x.name; }).join(", "); f.classList.add("con-foto"); }
      }
    });
    quien();
  });

  /* ---------- Formularios: sello de tiempo, recuperar lo escrito y avisos de vuelta ---------- */
  var q = w.location.search;
  function claveForm(f) { return "solvento-form-" + (f.getAttribute("data-form") || "contacto"); }
  function camposForm(f) { return [].filter.call(f.querySelectorAll("input[name], textarea[name], select[name]"), function (i) { return i.type !== "hidden" && i.type !== "file" && i.type !== "radio" && i.name !== "web"; }); }
  d.addEventListener("submit", function (e) {
    var f = e.target, t = f.querySelector && f.querySelector('input[name="t"]');
    if (t) t.value = Math.round(w.performance && performance.now ? performance.now() : 0);
    if (!f.querySelectorAll) return;
    var datos = {}; camposForm(f).forEach(function (i) { datos[i.name] = i.value; });
    try { sessionStorage.setItem(claveForm(f), JSON.stringify(datos)); } catch (x) {}
  }, true);
  var errForm = /[?&]enviado=0/.test(q), okForm = /[?&]enviado=1/.test(q);
  if (errForm || okForm) d.querySelectorAll("form[data-form]").forEach(function (f) {
    var k = claveForm(f);
    try {
      if (okForm) { sessionStorage.removeItem(k); return; }
      var datos = JSON.parse(sessionStorage.getItem(k) || "null"); if (!datos) return;
      camposForm(f).forEach(function (i) { if (datos[i.name] && !i.value) i.value = datos[i.name]; });
    } catch (x) {}
  });
  var ok = d.getElementById("form-ok"), ko = d.getElementById("form-error");
  if (ok && okForm) {
    ok.hidden = false;
    var fo = ok.closest("form");
    if (fo) { [].forEach.call(fo.children, function (ch) { if (ch !== ok) ch.hidden = true; }); fo.classList.add("form--hecho"); }
  }
  if (ko && errForm) {
    ko.hidden = false;
    var mm = /[?&]motivo=([a-z_\-]+)/i.exec(q);
    if (mm && mm[1] === "archivo") ko.textContent = "La foto no se ha podido adjuntar (formato o tamaño). Pruebe con otra, sin foto o llámenos al " + d.querySelector(".tel").textContent + ".";
  }
  var avisoVuelta = (ok && !ok.hidden && ok) || (ko && !ko.hidden && ko);
  if (avisoVuelta) {
    for (var pr = avisoVuelta; pr; pr = pr.parentElement) if (pr.classList && pr.classList.contains("rv")) pr.classList.add("dentro");
    if (w.requestAnimationFrame) requestAnimationFrame(function () { try { avisoVuelta.scrollIntoView({ block: "center" }); } catch (x) {} });
  }

  /* ---------- Cookies + GTM (solo en el dominio de producción y si hay contenedor) ---------- */
  var PROD = new RegExp("^(__HOSTS_RE__)$").test(w.location.hostname);
  var GTM = html.getAttribute("data-gtm");
  w.dataLayer = w.dataLayer || [];
  function gtag() { w.dataLayer.push(arguments); }
  var CLAVE = "__COOKIES__";
  function leer() { try { return localStorage.getItem(CLAVE); } catch (e) { return null; } }
  function guardar(v) { try { localStorage.setItem(CLAVE, v); } catch (e) {} }
  var eleccion = leer();
  gtag("consent", "default", { ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied", analytics_storage: "denied", wait_for_update: 500 });
  if (eleccion === "si") aceptar(true);
  function aceptar(silencioso) {
    gtag("consent", "update", { analytics_storage: "granted" });
    if (!silencioso) guardar("si");
  }
  if (okForm) w.dataLayer.push({ event: "formulario_enviado", formulario: (d.querySelector("[data-form]") || { getAttribute: function () { return ""; } }).getAttribute("data-form"), pagina: w.location.pathname });
  if (/enviado=/.test(q) && w.history && history.replaceState) {
    try { history.replaceState(null, "", w.location.pathname + w.location.hash); } catch (e) {}
  }
  var PAG = w.location.pathname;
  function ubicacion(a) {
    var zona = a.closest("[data-zona], .cab, .menu, .portada, .cab-int, .faq, .contacto, .pie, .barra-movil, section");
    return zona ? (zona.getAttribute("data-zona") || zona.className.split(" ")[0]) : "otro";
  }
  d.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a) return;
    var href = a.getAttribute("href");
    if (/^tel:/.test(href)) w.dataLayer.push({ event: "click_llamar", ubicacion: ubicacion(a), pagina: PAG, abierto: ABIERTO === true, numero: href.slice(4) });
    else if (/#presupuesto$/.test(href)) w.dataLayer.push({ event: "click_enviar_foto", ubicacion: ubicacion(a), pagina: PAG });
    else if (/maps\.google\.com\/\?cid/.test(href)) w.dataLayer.push({ event: "click_ficha_google", ubicacion: ubicacion(a), pagina: PAG });
    else if (/^mailto:/.test(href)) w.dataLayer.push({ event: "click_correo", ubicacion: ubicacion(a), pagina: PAG });
  }, true);
  d.addEventListener("focusin", function (e) {
    var f = e.target.form; if (!f || f._inicio || !/^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName) || e.target.type === "hidden") return;
    f._inicio = true;
    w.dataLayer.push({ event: "form_inicio", formulario: f.getAttribute("data-form") || "", campo: e.target.name || "", pagina: PAG });
  });
  d.addEventListener("invalid", function (e) {
    var f = e.target.form; if (!f) return;
    var ahora = Date.now(); if (f._err && ahora - f._err < 800) return;
    f._err = ahora;
    w.dataLayer.push({ event: "form_error", formulario: f.getAttribute("data-form") || "", campo: e.target.name || "", motivo: "validacion", pagina: PAG });
  }, true);
  if (errForm) {
    var mo = /[?&]motivo=([a-z_\-]+)/i.exec(q);
    w.dataLayer.push({ event: "form_error", motivo: mo ? mo[1] : "servidor", pagina: PAG });
  }
  if (PROD && GTM) {
    w.dataLayer.push({ "gtm.start": Date.now(), event: "gtm.js" });
    var s = d.createElement("script"); s.async = true; s.src = "https://www.googletagmanager.com/gtm.js?id=" + GTM;
    d.head.appendChild(s);
  }
  var aviso = d.getElementById("cookies");
  if (aviso && !eleccion) aviso.classList.add("visible");
  d.addEventListener("click", function (e) {
    var b = e.target.closest("[data-cookies]");
    if (!b) return;
    if (b.getAttribute("data-cookies") === "si") aceptar(false); else guardar("no");
    if (aviso) aviso.classList.remove("visible");
  });
  d.querySelectorAll("[data-cookies-config]").forEach(function (a) {
    a.addEventListener("click", function (e) { e.preventDefault(); if (aviso) aviso.classList.add("visible"); });
  });

  /* ---------- Barra fija del móvil: fuera mientras se ven los botones de la cabecera de la página ---------- */
  var barra = d.querySelector(".barra-movil"), acc = d.querySelector(".portada .acciones, .cab-int .acciones, .contacto__tel");
  if (barra && acc && "IntersectionObserver" in w) {
    new IntersectionObserver(function (ents) {
      barra.classList.toggle("barra-movil--fuera", ents[ents.length - 1].isIntersecting);
    }, { rootMargin: "0px 0px -88px 0px" }).observe(acc);
  }

  /* ---------- FAQ: una abierta a la vez (respaldo de <details name>) ---------- */
  d.querySelectorAll(".faq__lista").forEach(function (l) {
    l.addEventListener("toggle", function (e) {
      if (!e.target.open) return;
      l.querySelectorAll("details[open]").forEach(function (x) { if (x !== e.target) x.open = false; });
    }, true);
  });

  /* ---------- Apariciones (fade-anim de Archidex, más corto): desde abajo, una sola vez, escalonadas ---------- */
  var rv = d.querySelectorAll(".rv");
  if (reducido || !("IntersectionObserver" in w)) {
    rv.forEach(function (el) { el.classList.add("dentro"); });
  } else {
    var io = new IntersectionObserver(function (ents) {
      var k = 0;
      ents.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.style.setProperty("--d", (k++ * .08) + "s");
        en.target.classList.add("dentro"); io.unobserve(en.target);
      });
    }, { rootMargin: "0px 0px -6% 0px" });
    rv.forEach(function (el) { io.observe(el); });
  }
})();

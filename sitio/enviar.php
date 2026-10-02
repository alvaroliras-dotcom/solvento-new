<?php
/* Solvento · formularios de la web: presupuesto por foto (contacto) y candidatura (trabaja con nosotros).
   Antispam: trampa + tiempo en la página + sin enlaces en el mensaje. Sin captcha.
   Adjuntos: hasta 3 archivos de 8 MB (fotos; en la candidatura, también PDF y Word), comprobados por su
   contenido (finfo), no por la extensión. «t» lo rellena main.js: milisegundos con la página abierta. */
header('X-Robots-Tag: noindex');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: /contacto/'); exit; }
$c = function ($k, $max) { return trim(mb_substr(strip_tags($_POST[$k] ?? ''), 0, $max)); };
$tipo = ($_POST['tipo'] ?? '') === 'empleo' ? 'empleo' : 'presupuesto';
$pagina = $c('pagina', 120);
if (!preg_match('#^/[a-z0-9\-/]*$#', $pagina) || strpos($pagina, '//') !== false) { $pagina = '/contacto/'; }
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
    if ($_FILES['foto']['error'][$i] !== UPLOAD_ERR_OK || $_FILES['foto']['size'][$i] > 8 * 1048576) { $motivo = 'archivo'; break; }
    $tmp = $_FILES['foto']['tmp_name'][$i];
    $mime = $fi ? finfo_file($fi, $tmp) : '';
    if (!isset($tipos_ok[$mime])) { $motivo = 'archivo'; break; }
    $adj[] = ['nombre' => 'adjunto-' . ($i + 1) . '.' . $tipos_ok[$mime], 'mime' => $mime, 'datos' => file_get_contents($tmp)];
  }
}
$vuelta = $tipo === 'empleo' ? '/trabaja-con-nosotros/' : '/contacto/';
if ($motivo !== '') { header('Location: ' . $vuelta . '?enviado=0&motivo=' . $motivo . '#form-error'); exit; }
$para = 'info@solvento.es';
if ($tipo === 'empleo') {
  $asunto = 'CANDIDATURA · ' . $nombre . ' · ' . $oficio;
  $cuerpo = "Candidatura desde la web.\n\nNombre: $nombre\nTeléfono: $telefono\nOficio: $oficio\nAños de experiencia: $anios\nMunicipio: $donde\n\n$mensaje\n";
} else {
  $quien_t = $quien === 'particular' ? 'Particular' : 'Administrador o comunidad';
  $asunto = 'PRESUPUESTO · ' . $necesita . ' · ' . $nombre . ($comunidad ? ' (' . $comunidad . ')' : '');
  $cuerpo = "Petición de presupuesto desde la web.\n\nQuién: $quien_t\nNombre: $nombre\nTeléfono: $telefono\nCorreo: $correo\nAdministración o comunidad: $comunidad\nDirección o municipio: $donde\nQué necesita: $necesita\n\n$mensaje\n\nFotos adjuntas: " . count($adj) . "\nPágina: https://solvento.es$pagina\n";
}
$asunto = '=?UTF-8?B?' . base64_encode($asunto) . '?=';
$sep = 'sep-' . bin2hex(random_bytes(8));
$cab = "From: Web Solvento <web@solvento.es>\r\n" . ($correo !== '' ? "Reply-To: $correo\r\n" : '') . "MIME-Version: 1.0\r\nContent-Type: multipart/mixed; boundary=\"$sep\"\r\n";
$m = "--$sep\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n\r\n$cuerpo\r\n";
foreach ($adj as $a) {
  $m .= "--$sep\r\nContent-Type: {$a['mime']}; name=\"{$a['nombre']}\"\r\nContent-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"{$a['nombre']}\"\r\n\r\n" . chunk_split(base64_encode($a['datos'])) . "\r\n";
}
$m .= "--$sep--";
$enviado = @mail($para, $asunto, $m, $cab);
header('Location: ' . $vuelta . '?enviado=' . ($enviado ? '1#form-ok' : '0&motivo=envio#form-error'));

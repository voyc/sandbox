<!doctype html>
<html>
<head>
<meta http-equiv=Content-Type content="text/html; charset=UTF-8">
<meta name='viewport' content='width=device-width, initial-scale=1, maximum-scale=1'>
<title>sandbox index.php</title>
</head>
<body>
<h1>index.php</h1>

<?php echo "File suffix .php means PHP sections are interpreted."; ?>

<h2>Directory Index</h2>
By default, with no .htaccess directive, the default page for a folder is defined as</br>
<b>DirectoryIndex index.php index.cgi index.html</b></br>
<h2>Filename Suffix</h2>
The suffix lets Apache know how to preprocess the file.</br>
<ul>
<li>
<a href=index.cgi>index.cgi</a></br>
By default a2hosting created a cgi-bin directory when I created the subdomain, 
but the script runs from any folder.</br>
</li>
<li>
<a href=index.php>index.php</a></br>
This file is suffixed with .php, so php sections are interpreted.</br>
Most likely this is implemented with mod_php which allows for mixed html and php.</br>
</li>
<li>
<a href=index.html>index.html</a></br>
Straight HMTL.  PHP sections are ignored.</br>
</li>
</ul>
</body>
</html>

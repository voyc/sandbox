#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

#print "<!doctype html>"  # this causes a 500 error

print "Content-Type: text/html;charset=utf-8" # this is required, lest the browser try to save the file.
print

print "<html>"
print "<head>"
print "<meta http-equiv=Content-Type content='text/html; charset=UTF-8'>"
print "<meta name='viewport' content='width=device-width, initial-scale=1, maximum-scale=1'>"
print "<title>sandbox index.cgi</title>"
print "</head>"
print "<body>"
print "<h1>index.cgi</h1>"
print "This is a python script written for cgi.<br/>"
print "By default a2hosting created a cgi-bin directory when I created the subdomain, but the script runs from any folder.</br>"

print "<h2>Directory Index</h2>"
print "By default, with no .htaccess directive, the default page for a folder is defined as</br>"
print "<b>DirectoryIndex index.php index.cgi index.html</b></br>"
print "<h2>Filename Suffix</h2>"
print "The suffix lets Apache know how to preprocess the file.</br>"
print "<ul>"
print "<li>"
print "<a href=index.cgi>index.cgi</a></br>"
print "By default a2hosting created a cgi-bin directory when I created the subdomain, "
print "but the script runs from any folder.</br>"
print "</li>"
print "<li>"
print "<a href=index.php>index.php</a></br>"
print "This file is suffixed with .php, so php sections are interpreted.</br>"
print "Most likely this is implemented with mod_php which allows for mixed html and php.</br>"
print "</li>"
print "<li>"
print "<a href=index.html>index.html</a></br>"
print "Straight HMTL.  PHP sections are ignored.</br>"
print "</li>"
print "</ul>"
print "</body>"
print "</html>"

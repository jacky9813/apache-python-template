#!/usr/bin/env python3
import cgi
import json
import sys, pkg_resources, platform, os

# Header

print("Content-Type: text/html; charset=UTF-8")
print("")

# Content
print("""<!DOCTYPE html>
<html>
<head>
<title>python info</title>
<style>
td, th{
width: auto;
min-width: 400px;
border: 1px black solid;
padding: 0 5px;
}
td:nth-child(1), th:nth-child(1){
width: auto;
min-width: 150px;
text-align: right;
}
table{
border-collapse: collapse;
}
</style>
</head>
<body>
""")

# Print version info

print("""<table>
<tr><td>System Version</td><td>%s</td></tr>
<tr><td>Python Version</td><td>%s</td></tr>
<tr><td>Server Software</td><td>%s</td></tr>
</table><hr>""" % (platform.platform(), sys.version, os.environ["SERVER_SOFTWARE"]))

# Print Package info

print("""<h3>Installed Packages</h3>
<table>
<tr><th>Package Name</th><th>Version</th></tr>""")

for i in sorted(pkg_resources.working_set, key=lambda i : i.key):
    print("<tr><td>%s</td><td>%s</td></tr>" % (i.key, i.version))

print("</table><hr>")

# Print Environment Info

print("""<h3>Environment Info</h3>
<table>
<tr><th>Key</th><th>Value</th></tr>""")

for i in sorted(os.environ.keys()):
    print("<tr><td>%s</td><td>%s</td></tr>" % (i, os.environ[i]))

print("</table><hr>")

print("""</body>
</html>""")

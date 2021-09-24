import time
import urllib.request
import os
import re
from datetime import datetime
import phantomjs
import js2py
from requests_html import HTML

premenu = "kein menu"
premenu = os.popen("node nahrungsparser.js").read()

auswahl = []

premenu = premenu.split("""class="pre-wrap">""")
for i in range(len(premenu)):
    if i != 0:
        menuentry = premenu[i].split("""</span>""")[0]
        menuentry = menuentry.replace("'","")
        menuentry = menuentry.replace("+", "")
        menuentry = re.sub('\n', '',menuentry)
        menuentry = menuentry.replace("""\\n""", ' ')
        menuentry = menuentry.replace("      ", " ")
        auswahl.append(menuentry)

print(auswahl)

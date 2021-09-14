import time
import urllib.request
import os
from datetime import datetime

url ="https://cdn3.qnips.com/release-menu-pdfs/Mittagessen_DE_"+"37_20210913"+"_"+"668875"+".pdf"
urllib.request.urlretrieve(url, "tmp/tmp.pdf")



print(os.system('python pdf2txt.py tmp/tmp.pdf'))

time.sleep(5)

if os.path.exists("tmp/tmp.pdf"):
  os.remove("tmp/tmp.pdf")
else:
  print("Du hast hart verkaggert")
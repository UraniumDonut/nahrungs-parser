import time
import urllib.request
import os

url ="https://cdn3.qnips.com/release-menu-pdfs/Mittagessen_DE_37_20210913_668875.pdf"
urllib.request.urlretrieve(url, "tmp/tmp.pdf")
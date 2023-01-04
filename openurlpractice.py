from urllib.request import urlopen
import re

url = "http://ufcstats.com/fighter-details/f4c49976c75c5ab2"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("URL: ")
count = int(input("Count: "))
position = int(input("Position: "))

names = []

while count > 0:
    print("retrieving: {0}".format(url))
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup('a')
    name = anchors[position - 1].string
    names.append(name)
    url = anchors[position - 1]['href']
    count -= 1

print(names[-1])

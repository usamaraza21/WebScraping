from cgi import print_form
from cgitb import text
from importlib.resources import as_file
from xml.dom.minidom import TypeInfo
from bs4 import BeautifulSoup

with open("index.html" , "r") as f:
    doc = BeautifulSoup(f , "html.parser")

#print(doc.prettify())

aTag = doc.find("a")
hreftag = aTag['href']
print(hreftag)


#print(aTag)

# print("href = " , hreftag)


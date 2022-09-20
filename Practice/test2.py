from pydoc import doc
from bs4 import BeautifulSoup
with open("index2.html" , 'r') as f2:
    docc = BeautifulSoup(f2 , 'html.parser')
#print(docc.prettify())
optionTag = docc.find_all('option')
for i in optionTag:
    print(i.text)
    
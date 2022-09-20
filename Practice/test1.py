from cProfile import label
from cgitb import text
from turtle import title
from urllib import request
from bs4 import BeautifulSoup
import requests

urll = "https://www.czone.com.pk/graphic-cards-nvidia-geforce-winfast-leadtek-geforce-rtx-3050-hurricane-white-edition-8g-video-graphics-card-pakistan-p.13368.aspx"
_webpag = requests.get(urll)
_htmlFil = BeautifulSoup(_webpag.text , "html.parser")
#print(_htmlFil.prettify())
# _titlee = _htmlFil.find_all("title")                               #_htmlFil.title.string
# print(_titlee)

_prices = _htmlFil.find('span' , attrs={'class':'price-sales' , 'id': 'spnCurrentPrice'})
print(_prices.text)



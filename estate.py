import requests
from bs4 import BeautifulSoup

H_USERAGENT={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}

def req_to_soup(url, hdrs = H_USERAGENT):
    r = requests.get(url, headers = hdrs)
    cont = r.content
    return BeautifulSoup(cont, "html.parser")


SRC_URL = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"
html_estate = req_to_soup(SRC_URL)

rows = html_estate.find_all('div', {'class':'propertyRow'})

print(rows)

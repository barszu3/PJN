import re
import urllib.request

items =[]
links = ["https://www.ceneo.pl/Szlifierki_i_polerki/Rodzaj:Szlifierki_katowe;0020-30-0-0-2.htm", "https://www.ceneo.pl/Szlifierki_i_polerki/Rodzaj:Szlifierki_katowe;0020-30-0-0-3.htm"
         , "https://www.ceneo.pl/Szlifierki_i_polerki/Rodzaj:Szlifierki_katowe;0020-30-0-0-4.htm", "https://www.ceneo.pl/Szlifierki_i_polerki/Rodzaj:Szlifierki_katowe;0020-30-0-0-1.htm"]


for link in links:
    response = urllib.request.urlopen(link)
    page_source = response.read()
    items += re.findall(r'data-source-tag="">([A-Za-z0-9 ]+)</a>', page_source.decode('utf-8'))
print(set(items))
print(len(set(items)))
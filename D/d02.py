import re
import urllib.request


links = ["https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2008/2009)",
         "https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2009/2010)",
         "https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2010/2011)",
         "https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2011/2012)",
         "https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2012/2013)",
         "https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2013/2014)",
         "https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2014/2015)",
         "https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2015/2016)",
         "https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2016/2017)",
         "https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2017/2018)"]
Dict = {}
def checkOneYear(dict,input):
    items = []
    itemsPkt = []
    response = urllib.request.urlopen(input)
    page_source = response.read()
    items += re.findall(r'<td align="left"><a href="/wiki/.*">([A-Za-z0-9ńąłóŁŚźę\- ]+)</a>', page_source.decode('utf-8'))
    itemsPkt += re.findall(r'<td><b>([0-9]+)</b>', page_source.decode('utf-8'))
    x=0
    end = 0
    for team in items:
        if not team in Dict:
            Dict[team]=itemsPkt[x]
            x += 1
        else:
            value = int(Dict[team])
            sum = value + int(itemsPkt[x])
            x += 1
            Dict[team]=sum
        end += 1
        if end == 16:
            break
    print(Dict.items())

for link in links:
    checkOneYear(Dict, link)
print(Dict.items())
import requests 
from bs4 import BeautifulSoup
import re
# copy this '()'
proxy = {}
def proxy_port():
    r = requests.get("https://free-proxy-list.net")
    tr = BeautifulSoup(r.content,'lxml').find_all("tr")
    number = 0
    for port in tr:
        proxy_search = re.findall("<td>(\d.*?)</td>",str(port))
        panjang = len(proxy_search)
        if proxy_search and panjang == 2:
            number +=1
            proxy[str(number)] = proxy_search[0] + ":" + proxy_search[1]
proxy_port()
print(proxy)
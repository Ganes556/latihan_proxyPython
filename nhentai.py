from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1
import requests,re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
# pakai module https://pypi.org/project/free-proxy/
# code error karna proxy anjim
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
save_point = {}
def nekopoi(ip,main_url):

    session = requests.session()
    session.proxies = {"https":"https://"+ip,"http":"http://"+ip}
    # r = session.get("https://api.github.com/user",auth= HTTPBasicAuth('gustiganes@gmail.com', 'ghanes123456789'))
    r = session.get(main_url)
    soup = BeautifulSoup(r.content,"lxml")
    list_link = soup.find_all("a")
    for link in list_link:
        text = link.get_text()
        a = link.get("href").replace("\n","")
        link = urljoin(main_url,a)
        
        if "https://nhentai.net/g/" in link:
            nuklir_search = re.search("\d\d\d\d\d\d",link)
            nuklir = nuklir_search.group()
            save_point[nuklir] = text  
        if "page" in link :
            page_search = re.search("\d.*",link)
            page = page_search.group()
            run("https://nhentai.net?page="+page)
def run(main_url):
    global proxy
    for i in proxy.values():
        try:
            nekopoi(i,main_url)
            break
        except Exception:
            pass
try:
    run("https://nhentai.net")
except KeyboardInterrupt:
    for x,y in save_point.items():
        print(f"{x} -- > {y}")
for x,y in save_point.items():
    print(f"{x} -- > {y}")

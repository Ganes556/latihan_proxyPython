import requests 
from bs4 import BeautifulSoup
# session = requests.session()
# session.proxy = {"http":"http://89.109.8.160:21231","https":"https://89.109.8.160:21231"}

r = requests.get("http://nekopoi.care")
if "<title>Internet Positive" not in str(r.content):
    print(r.text) 
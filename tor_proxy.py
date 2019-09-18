import requests 
# copy this '()'
def get_tor_session():
    session = requests.session()
    session.proxies = {
        "http":"socks5://127.0.0.1:9050",
        "https":"socks5://127.0.0.1:9050"
    }
session = get_tor_session()
r = session.get('http://google.com')
print requests.get('http://httpbin.org/ip')
from stem import Signal
from stem.control import Controller
def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="admin1234")
        controller.signal(Signal.NEWNYM) # buat baru setiap detiknya 
renew_connection()
# session = get_tor_session()
print(session.get('http://nekopoi.care'))
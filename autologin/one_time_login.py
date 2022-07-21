import requests
from animation import Animation as An

payload = {'mode': '191', 'username': 'f20190896', 'password': 'fd531372'}


with requests.Session() as s:
    url = 'https://campnet.bits-goa.ac.in:8090/login.xml'
    r = s.post(url, data=payload)
    An.animation("Logging in", buffering_time=1)
    print('logged in')
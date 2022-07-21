import time
import requests

payload= {'mode': '191', 'username': 'f20190896', 'password': 'fd531372'}
while True:
    with requests.Session() as s:
        url = 'https://campnet.bits-goa.ac.in:8090/login.xml'
        r = s.post(url, data=payload)
    time.sleep(60)
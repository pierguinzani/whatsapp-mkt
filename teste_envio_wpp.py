# -*- coding: utf-8 -*-
import requests
import time
numeros = ['5598991030037', '5598991055667']
for numero in numeros:
    payload = numero
    code = "http://127.0.0.1:3400/whatsapp/" + payload + "/Essa%20mensagem%20foi%20gerada%20automaticamente%20e%20zanoni%20é%20um%20gay/"
    r = requests.get(code)
    print(r.url)
    time.sleep(15)
    

import requests
import json 

def Proxycek():
    geturl = 'https://www.proxyscan.io/api/proxy?format=json&type=socks5&limit=1&last_check=300&ping=100'
    r = requests.get(geturl).json()
    ip = r[0]['Ip']
    port = r[0]['Port']
    ipport = str(ip)+':'+str(port)
    return ipport

def Proxy():
    while True:
        try:
            testurl = 'https://wtfismyip.com/json'
            ipport = Proxycek()
            httpip = 'socks5://'+ipport
            httpsip = 'socks5://'+ipport
            test = requests.get(testurl,timeout=1,proxies={'http':httpip,'https':httpsip})
            test_icerik = test.json()
            print(test_icerik)
            
            return ipport
            break
        except:
            pass
from bs4 import BeautifulSoup
from xml.etree import ElementTree
import json
import requests

def ierParser():
    
    key = 'BV359oacvun7ZaVBlnAuPnLq3bj7AxJbVK8jdrWotyJwuQNVUP96aQ4XJNBiEdc8kMlPbvi3RVBaeZ5mONmvxNBEPlZQqyjPWKLip73jrFoEOe2uSYT00rKXKg90VRNdvvEUOW7QUDDsi60vsp8RfsYoAxXI8DNZ1LSdZig5bCgxnbzOqNHqT67DWZTa8zSQzo1WnWVKICzcMlBi8Jbu5hG4NPGAOF6muP88kckT27hQHf0vYvcyXhVRi6IXQV5DFNs6mC7giH27AzxsZUmcnHOM4qaoTMCgCdK3w4IVy5PPpXRsJa86tdZ78gC6mTMWFV5gp35eLQor29ggYre3NGxjEM5Q1Mset3KUcvDPeducysF99fh5yTI8hWcc8om8iJ88yMDnnPYuVVuVG5RWoxqZvMwGTlR00w4otHLxc4Rj5YmMlGWCXQTudjMmZ7UC7h3jbFl8ue4ufGdXjkeMOOdkcJKK4iXekPmXfDufeXS2WjOXFzDydHxsESHR5aEL'
    uid = 'ulju'
    url = 'https://IERNet.kins.re.kr/IERNet.asmx/jsonData?UID={uid}&AKEY={key}'.format(uid= uid,key= key)
    req = requests.get(url)
    if req.status_code == 200:
            
        html = req.text 
        jsonStr = html.replace('<?xml version="1.0" encoding="utf-8"?>','')
        jsonStr = jsonStr.replace('<string xmlns="http://tempuri.org/">','')
        jsonStr = jsonStr.replace('</string>','')
        print(jsonStr,type(jsonStr))
        result = json.loads(jsonStr)
        testlist1=[]
        testlist2=[]
        testlist3=[]
        testlist4=[]
        
        for i in range(len(result)):
            testlist1.append(result[i]['name'])
            testlist2.append(result[i]['erm'])
            testlist3.append(result[i]['unit'])
            testlist4.append(result[i]['time'])
        print(testlist1,'절취선',testlist2,'절취선2',testlist3,'인생절취',testlist4)

    else :
        print('잦은요청 시도',req.status_code, req, type(req)) 


if __name__ == "__main__":
    ierParser()
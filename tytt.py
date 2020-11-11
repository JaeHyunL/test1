#import urllib.request
#from urllib.parse import urlencode, quote_plus, unquote
import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree
import psycopg2

"""
conn = psycopg2.connect(host='localhost', dbname='Test',user='postgres',password='1234',port=5432)

cur = conn.cursor()
cur.execute("SELECT version();")
record = cur.fetchone()
print("You are connected to - ", record,"\n")

#cur.execute("CREATE TABLE yy (title varchar, content text);")
## Insert 구문
print(Parser.radiationParser())
cur.execute("INSERT INTO radiation.radiationtable (where2, time ,name  ,value ) VALUES (%s, %s,%s,%s)", ('공공데이터', '숙제!','ㅇㅅㅇ','ㅅㅅ',))
print("INSERT INTO yy (TITLE, CONTENT) VALUES ({a},{b})".format(a="dsd",b='sds'))
conn.commit()

print(cur.execute("SELECT * FROM yy "))

cur.close()
"""
            trueUrl='http://www.khnp.co.kr/environ/service/realtime/{wha}?serviceKey={key}&genName={keyword}'.format(wha=wha ,key=key,keyword=keyword)

# KEWROD LIST  , WS : 월성 KR : 고리 YK : 한빛 UJ : 한울 SU : 새울

keywordlist = ["WS","KR","YK","UJ","SU"]
for i in range(len(keywordlist)):
    keyword=keywordlist[i]
    key='bMkM%2FSABk%2BZWxCygmK%2FjiC1l0m%2FcEOA5SWWYGGM4IJNBVoJCjxKGhz9LXSXL9lnDIxP%2FhmHc2%2F3Tyfdbk2p2Hg%3D%3D'
    trueUrl='http://www.khnp.co.kr/environ/service/realtime/weather?serviceKey={key}&genName={keyword}'.format(key,keyword)
    # TEMP
    # 
    #  URL http://www.khnp.co.kr/environ/service/realtime/weather?servicekey=genName=
    print(trueUrl)
    req = requests.get(trueUrl)
    html =req.text
    soup= (BeautifulSoup(html,'html.parser'))
    str_xml = soup.prettify()
    #print(str_xml)
    root_element = ElementTree.fromstring(str_xml)
    iter_element = root_element.iter(tag="item")
    #print(iter_element)
    whichslist = [] 
    for element in iter_element : 
        whichdict = {}
        whichdict['expl']= element.find('expl').text
        whichdict['name'] = element.find('name').text
        whichdict['time'] = element.find('time').text
        whichdict['value'] = element.find('value').text
        whichslist.append(whichdict)

    conn = psycopg2.connect(host='localhost', dbname='Test',user='postgres',password='1234',port=5432)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("You are connected to - ", record,"\n")
    for i in range(len(whichslist)):
        where = whichslist[i]['expl'].replace('\n','')
        where = where.replace(' ','',6)
        time = whichslist[i]['time'].replace('\n','')
        time = time.replace(' ','',6)
        name = whichslist[i]['name'].replace('\n','')
        name = name.replace(' ','',6)
        value = whichslist[i]['value'].replace('\n','')
        value = value.replace(' ','',6) 
        print(where,time,name,value)
        try : 
           cur.execute("INSERT INTO {keyword}.{whatable} (where2, time ,name  ,value ) VALUES ({},{},{},{})".format(keyword=keyword,radiatontable=wha,where,time,name,value))
        except : 
            print('error' )
            continue 
    conn.commit()

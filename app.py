from flask import Flask ,render_template ,request
from crud import CRUD
from bs4 import BeautifulSoup
from xml.etree import ElementTree

import requests
app = Flask(__name__)

@app.route('/index',methods=['GET'])
def index():
    if request.method == 'GET' :
        arg = request.args.get('keword')
        cr = CRUD()
        result = cr.readData(arg)
        print(result)
    return "hellow flask"+arg

@app.route('/index2',methods=['GET'])
def index2():
    if request.method =="GET" :
        keywordlist = ["WS","KR","YK","UJ","SU"]
        for i in range(len(keywordlist)):
            keyword=keywordlist[i]
            key='bMkM%2FSABk%2BZWxCygmK%2FjiC1l0m%2FcEOA5SWWYGGM4IJNBVoJCjxKGhz9LXSXL9lnDIxP%2FhmHc2%2F3Tyfdbk2p2Hg%3D%3D'
            trueUrl='http://www.khnp.co.kr/environ/service/realtime/radiorate?serviceKey={key}&genName={keyword}'.format(key=key,keyword=keyword)
            req = requests.get(trueUrl)
            html =req.text
            soup= (BeautifulSoup(html,'html.parser'))
            str_xml = soup.prettify()
            root_element = ElementTree.fromstring(str_xml)
            iter_element = root_element.iter(tag="item")
            whichslist = [] 
            for element in iter_element : 
                whichdict = {}
                whichdict['expl']= element.find('expl').text
                whichdict['name'] = element.find('name').text
                whichdict['time'] = element.find('time').text
                whichdict['value'] = element.find('value').text
                whichslist.append(whichdict)

            for i in range(len(whichslist)):
                where = whichslist[i]['expl'].replace('\n','')
                where = where.replace(' ','',6)
                time = whichslist[i]['time'].replace('\n','')
                time = time.replace(' ','',6)
                name = whichslist[i]['name'].replace('\n','')
                name = name.replace(' ','',6)
                value = whichslist[i]['value'].replace('\n','')
                value = value.replace(' ','',6)  
                print('tyty')
                try:
                    db = CRUD()
                    db.insertData(keyword=keyword, where=where,time=time,name=name,value=value)
                except Exception as e :
                    print('errorpoint 2',e)
                    continue
        return "hellow flask2"
   
    



app.run(host="0.0.0.0",port=9999)

from flask import Flask ,render_template ,request , jsonify
from crud import CRUD
from bs4 import BeautifulSoup
from xml.etree import ElementTree
import json
import requests
app = Flask(__name__)


@app.route('/index',methods=['GET'])
def index():
    if request.method == 'GET' :
        arg = request.args.get('keyword')
        cr = CRUD()
        result = cr.readData(arg)
        resulti = cr.readtemp(arg)
        finalResult = {
            
        }

        for i in range(len(resulti)) :
            finalResult[i+1] = resulti[i]
            finalResult[(i+1)*100] = result[i]
        finalResult= json.dumps(finalResult ,ensure_ascii=False ,indent=4)
        print(finalResult,type(finalResult))
    return finalResult

@app.route('/index2',methods=['GET'])
def index2():
    key='bMkM%2FSABk%2BZWxCygmK%2FjiC1l0m%2FcEOA5SWWYGGM4IJNBVoJCjxKGhz9LXSXL9lnDIxP%2FhmHc2%2F3Tyfdbk2p2Hg%3D%3D'
    keywordlist = ["WS","KR","YK","UJ","SU"]
    if request.method =="GET" :
        wha = request.args.get('wha')
        for i in range(len(keywordlist)):
            keyword=keywordlist[i]
            trueUrl='http://www.khnp.co.kr/environ/service/realtime/{wha}?serviceKey={key}&genName={keyword}'.format(wha=wha ,key=key,keyword=keyword)
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
                time = time.replace(':','-')
                name = whichslist[i]['name'].replace('\n','')
                name = name.replace(' ','',6)
                value = whichslist[i]['value'].replace('\n','')
                value = value.replace(' ','',6)  
                try:
                    db = CRUD()
                    db.insertData(keyword=keyword,wha=wha ,where=where,time=time,name=name,value=value)
                except Exception as e :
                    print('errorpoint 2',e)
                    continue
        return "hellow flask2"
   
    


app.run(host="0.0.0.0",port=5000)

import schedule
import time
from apscheduler.schedulers.background import BackgroundScheduler
from crud import CRUD
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
from xml.etree import ElementTree
import json
import requests
app = Flask(__name__)


@app.route('/index', methods=['GET'])
def index():
    '''
        데이터 요청로직
        :input args : 지역 키워드 (WS,KR,YK,UJ,SU)
        :return :json data (기상정보,방사선수치)
    '''
    if request.method == 'GET':
        arg = request.args.get('keyword')
        arg2 = request.args.get('wha')
        if arg == None:
            arg = arg2
        db = CRUD()
        result = db.readData(keyword=arg, wha=arg2)
        finalResult = {

        }
        for i in range(len(result)):
            finalResult[i+1] = result[i]
            finalResult[(i+1)*100] = result[i]
        finalResult = json.dumps(finalResult, ensure_ascii=False, indent=4)
        #print(finalResult,type(finalResult))
    return finalResult


@app.route('/index2', methods=['GET'])
def index2():
    '''
        db 추가로직. 
        :input wha: = 검색 키워드 radiorate or weather
        :return: None
    '''
    key = 'bMkM%2FSABk%2BZWxCygmK%2FjiC1l0m%2FcEOA5SWWYGGM4IJNBVoJCjxKGhz9LXSXL9lnDIxP%2FhmHc2%2F3Tyfdbk2p2Hg%3D%3D'
    keywordlist = ["WS", "KR", "YK", "UJ", "SU"]
    if request.method == "GET":
        #wha = request.args.get('wha')
        for ei in range(2):
            whalist = ['weather', 'radiation']
            wha = whalist[ei]
            for i in range(len(keywordlist)):
                keyword = keywordlist[i]
                trueUrl = 'http://www.khnp.co.kr/environ/service/realtime/{wha}?serviceKey={key}&genName={keyword}'.format(
                    wha=wha, key=key, keyword=keyword)
                req = requests.get(trueUrl)
                html = req.text
                soup = (BeautifulSoup(html, 'html.parser'))
                str_xml = soup.prettify()
                root_element = ElementTree.fromstring(str_xml)
                iter_element = root_element.iter(tag="item")
                whichslist = []
                for element in iter_element:
                    whichdict = {}
                    whichdict['expl'] = element.find('expl').text
                    whichdict['name'] = element.find('name').text
                    whichdict['time'] = element.find('time').text
                    whichdict['value'] = element.find('value').text
                    whichslist.append(whichdict)

                for i in range(len(whichslist)):
                    where = whichslist[i]['expl'].replace('\n', '')
                    where = where.replace(' ', '', 6)
                    time = whichslist[i]['time'].replace('\n', '')
                    time = time.replace(' ', '', 6)
                    time = time.replace(':', '-')
                    name = whichslist[i]['name'].replace('\n', '')
                    name = name.replace(' ', '', 6)
                    value = whichslist[i]['value'].replace('\n', '')
                    value = value.replace(' ', '', 6)
                    try:
                        db = CRUD()
                        db.insertData(
                            keyword=keyword, wha=wha, where=where,
                            time=time, name=name, value=value)
                    except Exception as e:
                        print('errorpoint 2', e)
                        continue
        return "hellow flask2"


@app.route('/init', methods=['GET'])
def ierParser():
    '''
        ier파싱로직 
        :input: None
        :return: None
    '''
    key = 'BV359oacvun7ZaVBlnAuPnLq3bj7AxJbVK8jdrWotyJwuQNVUP96aQ4XJNBiEdc8kMlPbvi3RVBaeZ5mO'\
        'NmvxNBEPlZQqyjPWKLip73jrFoEOe2uSYT00rKXKg90VRNdvvEUOW7QUDDsi60vsp8RfsYoAxXI8DNZ1LSdZig5bC'\
        'gxnbzOqNHqT67DWZTa8zSQzo1WnWVKICzcMlBi8Jbu5hG4NPGAOF6muP88kckT27hQHf0vYvcyXhVRi6IXQV5DFNs6m'\
        'C7giH27AzxsZUmcnHOM4qaoTMCgCdK3w4IVy5PPpXRsJa86tdZ78gC6mTMWFV5gp35eLQor29ggYre3NGxjEM5Q1Mset'\
        '3KUcvDPeducysF99fh5yTI8hWcc8om8iJ88yMDnnPYuVVuVG5RWoxqZvMwGTlR00w4otHLxc4Rj5YmMlGWCXQTudjMmZ'\
        '7UC7h3jbFl8ue4ufGdXjkeMOOdkcJKK4iXekPmXfDufeXS2WjOXFzDydHxsESHR5aEL'
    uid = 'ulju'
    url = 'https://IERNet.kins.re.kr/IERNet.asmx/jsonData?UID={uid}&AKEY={key}'.format(
        uid=uid, key=key)
    req = requests.get(url)
    if req.status_code == 200:

        html = req.text
        jsonStr = html.replace('<?xml version="1.0" encoding="utf-8"?>', '')
        jsonStr = jsonStr.replace('<string xmlns="http://tempuri.org/">', '')
        jsonStr = jsonStr.replace('</string>', '')
        result = json.loads(jsonStr)
        db = CRUD()
        for i in range(len(result)):
            db.insertIerData(name=result[i]['name'], erm=result[i]
                             ['erm'], unit=result[i]['unit'], time=result[i]['time'])

    else:
        print('잦은요청 시도', req.status_code, req, type(req))

    return 'hellow Flask'


@app.route('/soulkey', methods=['GET'])
def doesParser():
    '''
        does파싱로직
        :input: None
        :return: None
    '''
    url = 'http://210.123.176.49:9090/OpenApi/Export/Json/9e60dd49466f46209c616516f5860bf6'
    req = requests.get(url)
    html = req.text
    result = json.loads(html)
    result = result['openApiExportDeviceList']
    db = CRUD()
    for i in range(len(result)):
        db.insertDoseData(result[i]['id'], result[i]['name'], result[i]['modelcode'], result[i]['time'],
                          result[i]['unit'], result[i]['doserate'], result[i]
                          ['latitude'], result[i]['longitude'], result[i]['rainfall'], result[i]['temperature'],
                          result[i]['windspeed'], result[i]['winddirection'])
    return 'helloww Flask'


def clear():
    db = CRUD()
    keywordlist = ["WS", "KR", "YK", "UJ", "SU", 'radiation', 'dose']
    whalist = ['weather', 'iernet', 'radiation', 'dose']
    for i in range(len(keywordlist)):
        db.cleartable(whalist[i], keywordlist[i])


sched = BackgroundScheduler()
sched.start()
sched.add_job(ierParser, 'interval', seconds=90, id="_2")
sched.add_job(doesParser, 'interval', seconds=90, id="_3")


app.run(host="0.0.0.0", port=5000)

from flask import Flask ,render_template ,request , jsonify
from apscheduler.schedulers.background import BackgroundScheduler
app = Flask(__name__)
import time
def pyty():
    start = time.time()
 
    for i in range(355555455):
        i = i
    
    print("궁금하긴한데:", time.time() - start)

    
def typy():
    start = time.time()
    i = 0
    print("시차부적응자:", time.time() - start)


@app.route('/index',methods=['GET'])
def dhodlfjsl():
    return "sogul"
sched = BackgroundScheduler()    
sched.start()
sched.add_job(pyty , 'interval' , seconds=3, id='_1')
sched.add_job(typy, 'interval', seconds=3, id="_2")


app.run(host="0.0.0.0",port=5000)

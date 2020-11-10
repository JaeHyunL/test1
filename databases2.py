import psycopg2
from psycopg2.extras import RealDictCursor

class Databases():
    def __init__(self):
        self.db = psycopg2.connect(host='localhost', dbname='Test',user='postgres',password='1234',port=5432) 
        self.cursor = self.db.cursor()
        #cur = db.cursor()
        #cur.execute("SELECT version();")
        #record = cur.fetchone()
       # print("You are connected to - ", record,"\n")

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()

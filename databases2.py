import psycopg2


class Databases():
    def __init__(self):
<<<<<<< HEAD
        #self.db = psycopg2.connect(host='34.64.167.104', dbname='test',user='postgres',password='mysecretpassword ',port=5433) 
        self.db = psycopg2.connect(host='34.64.167.104', dbname='test',user='postgres',password='mysecretpassword',port=5433)
=======
        self.db = psycopg2.connect(host='34.64.167.104', dbname='test',user='postgres',password='mysecretpassword',port=5433) 
>>>>>>> 056a044edd44ea2912ad115ae85f1f4fcfbdb273
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

import psycopg2


class Databases():
    def __init__(self):
        self.db = psycopg2.connect(host='192.168.1.152', dbname='openapi',user='postgres',password='mysecretpassword',port=5433)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()

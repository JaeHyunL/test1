from databases2 import Databases

class CRUD(Databases):

    def readData(self,keyword):
        sql = "SELECT * FROM {}.radiationtable ;".format(keyword)
        try: 
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            return("error : {}".format(e))

        return result
    
    def readtemp(self,keyword):
        
        sql = "SELECT * FROM {}.weather ;".format(keyword)
        try: 
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            return("error : {}".format(e))

        return result
    

    def insertData(self,keyword,wha,where,time,name,value):
        if wha == 'radiorate':
            wha = 'radiationtable'
        sql = " INSERT INTO  {keyword}.{wha}  (where2, time ,name  ,value ) VALUES  ('{where}', '{time}', '{name}', '{value}') ;".format(keyword=keyword,wha=wha ,where=where,time= time,name=name,value=value)
       
       
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print("error22",e)

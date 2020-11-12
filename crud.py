from databases2 import Databases

class CRUD(Databases):

    def readData(self,keyword,wha):
        """
            input: keyword location code
            return: radiation table
        """
        sql = "SELECT * FROM {wha}.{keyword} ;".format(wha=wha,keyword=keyword)
        try: 
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            return("Log point 1-1 : {}".format(e))

        return result

    def insertData(self,keyword,wha,where,time,name,value):
        '''
            input1 : keyword location code
            input2 : search data 
            input3 : location name 
            input4 : time 
            input5 : name 
            input6 : value 
            return : None 
        '''
        if wha == 'radiorate':
            wha = 'radiation'
        sql = " INSERT INTO  {wha}.{keyword}  (point, time ,name  ,value ) VALUES  ('{point}', '{time}', '{name}', '{value}') ;".format(keyword=keyword,wha=wha ,point=where,time= time,name=name,value=value)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print("Log point 2 ",e) 

    def insertIerData(self,name,erm,unit,time):
        sql = " INSERT INTO iernet.iernet (name, erm , unit , time) VALUES ( '{name}' ,'{erm}' , '{unit}' , '{time}' ) ;".format(name=name , erm=erm, unit=unit , time=time)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e  :
            print("Log point 3 ",e)

    def insertDoseData(self,id,name,modelcode,time,unit,doserate,latitude,longitude,rainfall,temperatrue,windspeed,winddirection):
        sql = "INSERT INTO dose.dose (id,name,modelcode,time,unit,doserate,latitude,longitude,raintfall,temperatrue,windspeed,winddirection) "
        sql += "VALUES ('{id}','{name}','{modelcode}' , '{time}','{unit}','{doserate}','{latitude}','{longitude}','{rainfall}','{temperatrue}','{windspeed}' ,'{windspeed}' ) ;".format(id=id,name=name,modelcode=modelcode,time=time,unit=unit,doserate=doserate,latitude=latitude,longitude=longitude,rainfall=rainfall,temperatrue=temperatrue,windspeed=windspeed,winddirection=winddirection)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print("Log point 4" , e)

    def cleartable(self,wha,keyword):
        sql = "delete from {}.{}".format(wha,keyword)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print("Log Point 5", e)
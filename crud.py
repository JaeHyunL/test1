from databases2 import Databases

class CRUD(Databases):
'''
    CRUD class 
'''

    def readData(self,keyword):
        """
            input: keyword location code
            return: radiation table
        """
        sql = "SELECT * FROM {}.radiationtable ;".format(keyword)
        try: 
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            return("error : {}".format(e))

        return result
    
    def readtemp(self,keyword):
        '''
            input: keyword  location code 
            return: weather table 
        '''
        sql = "SELECT * FROM {}.weather ;".format(keyword)
        try: 
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            return("error : {}".format(e))

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
            wha = 'radiationtable'
        sql = " INSERT INTO  {keyword}.{wha}  (where2, time ,name  ,value ) VALUES  ('{where}', '{time}', '{name}', '{value}') ;".format(keyword=keyword,wha=wha ,where=where,time= time,name=name,value=value)
       
       
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print("error22",e)

from databases2 import Databases

class CRUD(Databases):

    def readData(self,keyword):

        sql = " SELECT * FROM {}.radiationtable ;".format(keyword)
        try: 
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            print(e)
            return("error : {}".format(e))

        return result


    def insertData(self,keyword,where,time,name,value):
        sql = " INSERT INTO {radiation}.radiationtable (where2, time ,name  ,value ) VALUES ({where}, {time}, {name}, {value}) ;".format(radiation=keyword, where= where,time= time,name = name,value=value)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print("error22",e)

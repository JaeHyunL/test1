import psycopg2

conn = psycopg2.connect(host='34.64.167.104', dbname='test',user='postgres',password='mysecretpassword',port=5433)

cur = conn.cursor()
cur.execute("SELECT version();")
record = cur.fetchone()
print("You are connected to - ", record,"\n")

#cur.execute("CREATE TABLE yy (title varchar, content text);")
## Insert 구문

cur.execute("SELECT * FROM UJ.radiationtable ;")
print("The number of parts: ", cur.fetchall())
print(cur.execute("SELECT * FROM UJ.radiationtable ;"))

conn.commit()
print(conn.commit())

cur.close()



# SELCET * FROM  radiation.radiationtable
# Querry SELECT * FROM radiation.radiationtable ;

import mysql.connector
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="Rickyp@w@r39"
)

#prepare a cursor object
cursorObject= dataBase.cursor()

#Crete a database
cursorObject.execute("create database elderco")
print("all done")
#Install mysql
#Pip install mysql
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='aJ941S@>A/<+'
)

#Prepare cursor object

cursorObject= dataBase.cursor()

#Create DB
cursorObject.execute("CREATE DATABASE ProbNet2")

print("Done")


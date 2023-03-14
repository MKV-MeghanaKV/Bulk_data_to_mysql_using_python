import pandas as pd
import mysql.connector

db = mysql.connector.connect(   host = "localhost",
                        user = "root",
                        password = "Mysql")
cursor = db.cursor()
cursor.execute('create database bulkdb')
cursor.execute('create table bulkdb.taskdata(col1 int,col2 int,col3 int,col4 int,col5 int,col6 int,col7 int,col8 int,col9 int,col10 int,col11 int,col12 int)')
data=pd.read_csv('glass.data')
print(data.head())
import MySQLdb

import sqlalchemy

from sqlalchemy import  create_engine



######Create Engine####



engine=create_engine("mysql+mysqldb://root:Mysql@127.0.0.1:3306/bulkdb")
conn=engine.connect()

print(engine);

###########Define your python code##############

def function_name():

    data = pd.read_csv('glass.data')   
    data_frame = data.to_sql('taskdata', con=engine, method='multi',index=False, if_exists='replace')

############Close Connection###############

conn = engine.raw_connection()

conn.commit()

function_name()
#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install mysql-connector-python


# In[40]:


import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='bus443',
                                         user='root',
                                         password='1J2o3r4d5y!')
    
    
    mySql_insert_query = """INSERT INTO faculty (firstname, lastname, coursename, courselocation) 
                           VALUES 
                           ('Jordan', 'Pippins', 'BUS443', 'Nelson') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()

    sql_select_Query = "select * from faculty into outfile 'output.csv' FIELDS TERMINATED BY ','         OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' FROM faculty"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    
    
    for row in records:
        print("firstname = ", row[0], )
        print("lastname = ", row[1])
        print("coursename  = ", row[2])
        print("courselocation  = ", row[3], "\n")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")


# In[ ]:





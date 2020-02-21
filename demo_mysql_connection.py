# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 01:01:04 2020

@author: Rajasekhar.Matam
"""

import mysql.connector

mydb = mysql.connector.connect(host = "localhost",user ="root", passwd = "",database = "mydatabase")

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("Create DATABASE mydatabase")
mycursor.execute("show databases")
for x in mycursor:
    print(x)
    
mycursor.execute("create table customers (name VARCHAR(255),address VARCHAR(255))")
#mycursor.execute("CREATE TABLE customer (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("show tables")
for x in mycursor:
    print(x)
    
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val =("john","26hyd")
mycursor.execute(sql,val)
mydb.commit()


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
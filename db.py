#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as db
import sys

con = db.connect('localhost', 'root', 'akshita')
cur = con.cursor(db.cursors.DictCursor)

with con:

 def create_db():
  cur.execute('DROP DATABASE IF Exists Box1')
  cur.execute('CREATE DATABASE Box1')
  cur.execute('USE Box1')

 def create_table():
  cur.execute('CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25), Post VARCHAR(25))')


 def insert_table():
  for i in range(10):
   cur.execute("INSERT INTO Writers(Name,Post) VALUES('Jack London','Employee')")
   
   con.commit()

  
 def retrieval():
    cur.execute("SELECT * FROM Writers LIMIT 5") 
    rows = cur.fetchall()
    desc = cur.description
    print "%s %3s" % (desc[0][0], desc[1][0])
    for row in rows:
      print row["Id"], row["Name"] ,row["Post"]


if __name__=="__main__":
    create_db()
    create_table()
    insert_table()
    retrieval()

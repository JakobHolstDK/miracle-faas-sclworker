#!/usr/bin/env python

import os
import psycopg2
conn = psycopg2.connect(
database="sclbuilder",
user="sclbuilder",
password="django2know")

req = str("we did it")
curr = conn.cursor()

curr.execute("SELECT * FROM Project;")
  
# FETCH ALL THE ROWS FROM THE CURSOR
data = curr.fetchall()
  
# PRINT THE RECORDS
for row in data:
    print(row)
  
# CLOSE THE CONNECTION
conn.close()


print(req)


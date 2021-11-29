#!/usr/bin/env python

import os
import psycopg2
conn = psycopg2.connect(
database="sclbuilder",
user="sclbuilder",
password="django2know")

req = str("we did it")
curr = conn.cursor()


curr.execute("DESCRIBE TABLE Project;")
data = curr.fetchall()
for row in data:
    print(row)
conn.close()


print(req)


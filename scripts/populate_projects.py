#!/usr/bin/env python

import os
import psycopg2
conn = psycopg2.connect(
database="sclbuilder",
user="sclbuilder",
password="django2know")

curr = conn.cursor()
curr.execute("                           \
            SELECT                       \
            table_name,                  \
            column_name,                 \
            data_type                    \
            FROM                         \
               information_schema.columns\
            WHERE                        \
               table_name = 'project';      \
   ")
data = curr.fetchall()
for row in data:
    print(row)
conn.close()


print(req)


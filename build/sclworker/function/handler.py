import os
import psycopg2
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    conn = psycopg2.connect(
    host="192.168.123.9",
    database="sclbuilder",
    user="sclbuilder",
    password="django2know")

    req = str("we did it") 
    
    return req

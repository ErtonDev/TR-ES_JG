# TR-ES_JG
# API
import psycopg2
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

HOST = os.getenv('DBHOST')
USER = os.getenv('DBUSER')
PASS = os.getenv('DBPASS')
NAME = os.getenv('DBNAME')



# CONNECT
def connect():
    try:
        conn = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASS,
            dbname=NAME
        )
        # Credentials not public
        return conn
    except Exception as error:
        # TODO(Erton): Instead of print should become a notification in our GUI
        print(f"ERROR: Failed to connect to database.\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}\n")



# GET
def get_user(conn, key, param):
    pass

def get_requests(conn, key, param):
    pass

def get_chat(conn, key, param):
    pass



# POST
def post_user(conn, user_id, user_name, user_pass):
    # Friends, days and valoration are unnecessary
    pass

def post_requests(conn, from_who, type, desc):
    pass

def post_chat(conn, ids):
    # Last is unnecessary
    pass



# PUT
def put_user(conn, key, param, value):
    pass

def put_global(conn, key, param, value):
    pass

def put_requests(conn, key, param, value):
    pass

def put_chat(conn, key, param, value):
    pass

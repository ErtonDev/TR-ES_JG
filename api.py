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

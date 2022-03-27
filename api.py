# API
import psycopg2
import os
from dotenv import load_dotenv

# load_dotenv will look for env variables
load_dotenv()

HOST = os.getenv('DBHOST')
USER = os.getenv('DBUSER')
PASS = os.getenv('DBPASS')
NAME = os.getenv('DBNAME')

# API functions...

# API
import psycopg2
import os
from dotenv import load_dotenv

# load_dotenv will look for env variables
# load_dotenv() NOTE(Erton): decomment once .env is ready
# TODO(Erton): Setup DB and create .env

HOST = "os.getenv('DBHOST')" # NOTE(Erton): decomment once .env is ready
USER = "os.getenv('DBUSER')"
PASS = "os.getenv('DBPASS')"
NAME = "os.getenv('DBNAME')"

# API functions...

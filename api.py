# TR-ES_JG
# API
import psycopg2
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')
DBNAME = os.getenv('DBNAME')



# CONNECT NOTE(Erton): conn.close() after creating conn = connect() closes connection
def connect():
    try:
        conn = psycopg2.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            dbname=DBNAME
        )

        # Credentials not public
        return conn

    except Exception as error:
        print(f"ERROR: Failed to connect to database.\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")
        return "f"



# GET
def get_users(conn, param, where, equals):
    try:
        cur = conn.cursor()
        cur.execute(f"""SELECT {param} FROM users WHERE {where} = {equals};""")
        result = cur.fetchall()
        cur.close()
        conn.commit()

        return result[0][0]

    except Exception as error:
        print(f"ERROR: Failed to GET data from USERS!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")
        return "f"

def get_users_column(conn, column):
    try:
        cur = conn.cursor()
        cur.execute(f"""SELECT {column} FROM users;""")
        result = cur.fetchall()
        cur.close()
        conn.commit()

        return result

    except Exception as error:
        print(f"ERROR: Failed to GET data from USERS!\nERROR INFO: {error}\nEXCEPTION TYPE {type(error)}")
        return "f"

def get_global(conn, param, where):
    try:
        cur = conn.cursor()
        cur.execute(f"""SELECT {param} FROM global WHERE subject = {where};""")
        result = cur.fetchall()
        cur.close()
        conn.commit()

        return result[0][0]

    except Exception as error:
        print(f"ERROR: Failed to GET data from GLOBAL!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")
        return "f"



# POST
def post_users(conn, user_id: int, user_name: str, user_pass: str,
               user_color: str, user_day1: list, user_day2: list, 
               user_day3: list, user_day4: list, user_day5: list, 
               user_day6: list, user_day7: list, user_friends: list,
               user_requests: list, user_connections: int,
               user_classes: list):
    try:
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO users(id, name, pass, color, day1, day2, day3, day4, day5, day6, day7, friends, requests, connections, classes)
        VALUES({user_id}, '{user_name}', '{user_pass}', '{user_color}', {user_day1}, {user_day2}, {user_day3}, {user_day4}, {user_day5}, {user_day6}, {user_day7}, {user_friends}, {user_requests}, {user_connections}, {user_classes});""")
        conn.commit()
        cur.close()

    except Exception as error:
        print(f"ERROR: Failed to POST data in USERS!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")
        return "f"

    else:
        conn.commit()



# PUT NOTE(Erton): If value is a string send str(f"'{value}'")
def put_users(conn, param, where, equals, value):
    try:
        cur = conn.cursor()
        cur.execute(f"""UPDATE users SET {param} = {value} WHERE {where} = {equals};""")
        conn.commit()
        cur.close()

    except Exception as error:
        print(f"ERROR: Failed to PUT data in USERS!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")
        return "f"

def put_global(conn, param, where, value):
    try:
        cur = conn.cursor()
        cur.execute(f"""UPDATE global SET {param} = {value} WHERE subject = {where};""")
        conn.commit()
        cur.close()

    except Exception as error:
        print(f"ERROR: Failed to PUT data in GLOBAL!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")
        return "f"



# DELETE
def delete_users(conn, where):
    try:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM users WHERE id = {where};")
        conn.commit()
        cur.close()

    except Exception as error:
        print(f"ERROR: Failed to DELETE data from USERS!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")
        return "f"

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
        # TODO(Erton): Instead of print should become a notification in our GUI
        print(f"ERROR: Failed to connect to database.\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")



# GET
def get_users(conn, param, where):
    try:
        cur = conn.cursor()
        cur.execute(f"""SELECT {param} FROM users WHERE id = {where};""")
        result = cur.fetchall()
        cur.close()
        conn.commit()

        return result[0][0]

    except Exception as error:
        print(f"ERROR: Failed to GET data from USERS!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")

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



# POST
def post_users(conn, user_id, user_name, user_pass,
               user_friends, user_color, user_day1, 
               user_day2, user_day3, user_day4, user_day5,
               user_day6, user_day7, user_description,
               user_mark, user_submitted, user_connections,
               user_prev):
    try:
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO users(id, name, pass, friends, color, day1, day2, day3, day4, day5, day6, day7, description, mark, submitted, connections, prev)
        VALUES({user_id}, '{user_name}', '{user_pass}', {user_friends}, '{user_color})', {user_day1}, {user_day2}, {user_day3}, {user_day4}, {user_day5}, {user_day6}, {user_day7}, '{user_description}', {user_mark}, {user_submitted}, {user_connections}, {user_prev});""")
        conn.commit()
        cur.close()

    except Exception as error:
        print(f"ERROR: Failed to POST data in USERS!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")

    else:
        conn.commit()


# PUT NOTE(Erton): If value is a string send str(f"'{value}'")
def put_users(conn, param, where, value):
    try:
        cur = conn.cursor()
        cur.execute(f"""UPDATE users SET {param} = {value} WHERE id = {where};""")
        conn.commit()
        cur.close()

    except Exception as error:
        print(f"ERROR: Failed to PUT data in USERS!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")

def put_global(conn, param, where, value):
    try:
        cur = conn.cursor()
        cur.execute(f"""UPDATE global SET {param} = {value} WHERE id = {where};""")
        conn.commit()
        cur.close()

    except Exception as error:
        print(f"ERROR: Failed to PUT data in GLOBAL!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")



# DELETE
def delete_users(conn, where):
    try:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM users WHERE id = {where};")
        conn.commit()
        cur.close()

    except Exception as error:
        print(f"ERROR: Failed to DELETE data from USERS!\nERROR INFO: {error}\nEXCEPTION TYPE: {type(error)}")

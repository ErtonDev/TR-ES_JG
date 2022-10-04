# Script for database migration
import api
import psycopg2
import bptools as bp

old = api.connect()
new = psycopg2.connect(host="ec2-52-30-75-37.eu-west-1.compute.amazonaws.com",
                       user="twzcddipwcqurh",
                       password="955ff24bdc82606aca3e9240ea12aa9ddeb5a59ff16f7463adde33c028c93611",
                       dbname="d12e872sjdkjnf")



# functions (post basically)
def post_new_users(conn, user_id: int, user_name: str, user_pass: str,
                   user_color: str, user_day1: list, user_day2: list,
                   user_day3: list, user_day4: list, user_day5: list,
                   user_day6: list, user_day7: list, user_friends: list,
                   user_requests: list, user_connections: int,
                   user_classes: list):
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO users(id, name, pass, color, day1, day2, day3, day4, day5, day6, day7, friends, requests, connections, classes)
    VALUES({user_id}, '{user_name}', '{user_pass}', '{user_color}', {user_day1}, {user_day2}, {user_day3}, {user_day4}, {user_day5}, {user_day6}, {user_day7}, {user_friends}, {user_requests}, {user_connections}, {user_classes});""")
    conn.commit()
    cur.close()

def post_new_global(conn, subject: str, value: int):
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO global(subject, next_id)
    VALUES('{subject}', {value})""")
    conn.commit()
    cur.close()



print("Migrating DB")
print("* Downloading TABLE (users)...", end="\r")

# users
all_user_id = api.get_users_column(old, "id")
all_user_name = api.get_users_column(old, "name")
all_user_pass = api.get_users_column(old, "pass")
all_user_color = api.get_users_column(old, "color")
all_user_day1 = api.get_users_column(old, "day1")
all_user_day2 = api.get_users_column(old, "day2")
all_user_day3 = api.get_users_column(old, "day3")
all_user_day4 = api.get_users_column(old, "day4")
all_user_day5 = api.get_users_column(old, "day5")
all_user_day6 = api.get_users_column(old, "day6")
all_user_day7 = api.get_users_column(old, "day7")
all_user_friends = api.get_users_column(old, "friends")
all_user_requests = api.get_users_column(old, "requests")
all_user_connections = api.get_users_column(old, "connections")
all_user_classes = api.get_users_column(old, "classes")

print("* Uploading data...", end="\r")

for i in all_user_id:
    j = all_user_id.index(i)

    post_new_users(new, 
                   all_user_id[j][0],
                   all_user_name[j][0],
                   all_user_pass[j][0],
                   all_user_color[j][0],
                   bp.format1DList(all_user_day1[j][0]),
                   bp.format1DList(all_user_day2[j][0]),
                   bp.format1DList(all_user_day3[j][0]),
                   bp.format1DList(all_user_day4[j][0]),
                   bp.format1DList(all_user_day5[j][0]),
                   bp.format1DList(all_user_day6[j][0]),
                   bp.format1DList(all_user_day7[j][0]),
                   bp.format1DList(all_user_friends[j][0]),
                   bp.format1DList(all_user_requests[j][0]),
                   all_user_connections[j][0],
                   bp.format2DList(all_user_classes[j][0])
                   )

# global
print("* Downloading TABLE (users)...", end="\r")
value = api.get_global(old, "next_id", "'user'")

print("* Uploading data...", end="\r")
post_new_global(new, "user", value)

print("Migration completed successfully!")

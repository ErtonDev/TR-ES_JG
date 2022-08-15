# This is a temporal file for API testing
# Remove before release of the final version

import api

conn = api.connect()

'''This is how lists are made on POST
result = api.post_users(
    conn,
    100000,
    "test_user",
    "password",
    "'{0, 0}'", 
    "blue",
    "'{"'none'", "'none'"}'",
    "'{"'none'", "'none'"}'",
    "'{"'none'", "'none'"}'",
    "'{"'none'", "'none'"}'",
    "'{"'none'", "'none'"}'",
    "'{"'none'", "'none'"}'",
    "'{"'none'", "'none'"}'",
    "Hola soy @test_user",
    11.0,
    0,
    1,
    "'{"'none'", "'none'"}'"
)
'''

'''Working new user creation
query = api.post_users(
    conn=conn,
    user_id=100000,
    user_name="test_user",
    user_pass="password",
    user_color="blue",
    user_day1="'{}'",
    user_day2="'{}'",
    user_day3="'{}'",
    user_day4="'{}'",
    user_day5="'{}'",
    user_day6="'{}'",
    user_day7="'{}'",
    user_friends="'{}'",
    user_requests="'{}'",
    user_connections=1,
    user_classes="'{}'"
)
'''

'''
got = api.get_users(conn, "day1", "id", 100000)

new_event = ["task", "100000", "0"]
old_event = ["note", "100012", "1"]
odd_event = ["eric", "100000", "0"]
got.append(new_event)
got.append(old_event)
got.append(odd_event)


# Formateador de lista a postgres Array
# Haré un archivo de boxpile_tools.py
super_counter = 0
max_super = len(got) - 1
msg = "'{"
for i in got:
    index_counter = 0
    max_index = len(i) - 1
    msg += "{"
    for j in i:
        if index_counter != max_index:
            msg += '"' + j + '",'
        else:
            msg += '"' + j + '"'
        index_counter += 1
    if super_counter != max_super:
        msg += "},"
    else:
        msg += "}"
    super_counter += 1
msg += "}'"
print(msg)



query = api.put_users(conn, "day1", 100000, msg)
# Lists on PUT: '{{"1","2"},{"3","4"}}'
'''

entered = "us"

query = api.get_users_column(conn, "name")

match = []
for i in query:
    for j in i:
        length = len(entered)
        if j[:length] == entered:
            match.append(j)
print(match)

conn.close()

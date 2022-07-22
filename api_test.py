# This is a temporal file for API testing
# Remove before release of the final version

import api

conn = api.connect()

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
conn.close()

# print(result)

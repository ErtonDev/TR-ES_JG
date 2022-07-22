# This is a temporal file for API testing
# Remove before release of the final version

import api

conn = api.connect()

# result = api.post_users(conn, 'next_id', "'user'", 100000)
conn.close()

# print(result)

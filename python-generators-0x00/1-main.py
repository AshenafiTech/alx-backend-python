#!/usr/bin/venv python3
from itertools import islice
stream_users_mod = __import__('0-stream_users')

# iterate over the generator function and print only the first 6 rows
for user in islice(stream_users_mod.stream_users(), 10):
    print(user)
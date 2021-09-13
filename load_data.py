import pandas as pd
import sqlite3
import os.path

db='./users.db'

if os.path.isfile(db):
    print('DB Exists nothing is added...')
else:
    print('Creating db...')
    file='data.json'
    df = pd.read_json(file)
    con = sqlite3.connect(db)
    df.to_sql('users',con)

con = sqlite3.connect(db)

# TEST if db is not empty
# users = pd.read_sql('select * from users limit 10',con)
# print(users)


import sqlite3
import pandas as pd
conn = sqlite3.connect('factbook.db')
q = "SELECT * FROM sqlite_master WHERE type = 'table';"

print(pd.read_sql_query(q, conn))

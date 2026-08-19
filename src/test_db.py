import pandas as pd
import sqlite3

conn = sqlite3.connect('data/patient_db.db')

query = "SELECT * FROM patients"
result_df = pd.read_sql_query(query, conn)
print(result_df)
conn.close()
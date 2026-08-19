import pandas as pd
import sqlite3

raw_patient_data = {
    'patient_id' : [1,2,3,4,5],
    'age' : [23,44,34,54,32],
    'gender' : ['male', 'female', 'female', 'male', 'female'],
    'cholesterol_level' : [180,220,178,238,190],
    'Diagnosis' : ['Healthy', 'Heart_Disease', 'Healthy', 'Heart_Disease', 'Healthy']
}

df = pd.DataFrame(raw_patient_data)
conn = sqlite3.connect('data/patient_db.db')
df.to_sql('patients', conn, index=False, if_exists='replace')
conn.close()
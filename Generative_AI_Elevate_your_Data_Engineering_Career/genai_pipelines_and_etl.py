"""

Write a Python code that reads a CSV file from a URL into a Pandas dataframe, and prints the first 5 entries to confirm it.

In a pandas dataframe, identify the categorical variables and perform label encoding on them

Write a python code that loads a python dataframe to an SQLite3 database named "Patient_record" as a table "Liver_patients". To confirm loading, query the database to print the first entries in the table.

"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import sqlite3

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-AI0273EN-SkillsNetwork/labs/v1/m2/data/Indian%20Liver%20Patient%20Dataset%20%28ILPD%29.csv"
df = pd.read_csv(url)

# Assuming df is your Pandas dataframe
categorical_cols = df.select_dtypes(include=['object']).columns

label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

#print(df.head())

# Assuming df is your Pandas dataframe
conn = sqlite3.connect('Patient_record.db')
df.to_sql('Liver_patients', conn, index=False)

# Query the database to print the first entries in the table
query = "SELECT * FROM Liver_patients LIMIT 5"
result = pd.read_sql(query, conn)
print(result)
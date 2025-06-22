"""
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-AI0273EN-SkillsNetwork/labs/v1/m2/data/laptop_pricing_dataset_base.csv"

Write a Python code that reads a csv record from a URL and does the following.
1. Identify the columns which have values as "?" in them.
2. Replace these with the mean value of the respective attribute. 
2. Modify the data type of the attribute to float after replacement.

For a data in a python dataframe, write a code that removes all duplicate entries from the data. Print the total number of rows in the data before and after removal, to prove the working of the code.

Write a python code to extract entries of a dataframe where the attribute 'Price' has outliers that might be anomalies in comparison to the other data.

"""


import pandas as pd
import numpy as np


# Read CSV record from URL
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-AI0273EN-SkillsNetwork/labs/v1/m2/data/laptop_pricing_dataset_base.csv"
data = pd.read_csv(url)
print(data.dtypes)

# Identify columns with "?" values
cols_with_question_mark = data.columns[data.isin(['?']).any()]
print(cols_with_question_mark)

# Replace "?" values with the mean value of the respective attribute
for col in cols_with_question_mark:
    mean_val = pd.to_numeric(data[col], errors='coerce').mean()
    data[col] = pd.to_numeric(data[col].replace('?', mean_val))

# Modify the data type of the attribute to float after replacement
data[cols_with_question_mark] = data[cols_with_question_mark].astype(float)

# Print the modified data
print(data.dtypes)

print("Total number of rows before removal:", len(data))

# Remove duplicate entries
data.drop_duplicates(inplace=True)

# Print the total number of rows after removal
print("Total number of rows after removal:", len(data))


# Assuming 'data' is the pandas DataFrame containing the data

# Calculate the mean and standard deviation of the prices
mean_price = data['Price'].mean()
std_price = data['Price'].std()

# Define a threshold for outliers (e.g., 3 standard deviations away from the mean)
outlier_threshold = 3

# Identify outliers using the threshold
outliers = data[(np.abs(data['Price'] - mean_price) > outlier_threshold * std_price)]

# Extract entries with price outliers
entries_with_outliers = data[data['Price'].isin(outliers['Price'])]

# Print the entries with price outliers
print("Entries with price outliers:")
print(entries_with_outliers)
#Name: RINASHINI A/P ARUNASALAM SUKORMARU
#Matric ID: WQD170077

import pandas as pd

# Importing the dataset and printing the first 5 rows of the dataset
df = pd.read_csv("dataset.csv")
print(df.head())



# Cleaning the column names of the dataset
print(df.columns.values)
df.columns = df.columns.str.strip().str.replace('[', '').str.lstrip()
print(df.columns.values)



# Determining number of missing values in each column
print(df.shape)
print(df[52:58])
## Replacing the blank values with "Nan"
df = df.replace(r'^\s*$', pd.np.NaN, regex=True)
print(df[52:58])
## Number of missing values in each column
col_missing = df.isnull().sum()
print(col_missing)



# Imputing the "NaN" with column mean values of the dataset
## Converting the values to numeric form
df['Date'] = pd.to_datetime(df['Date'])
df['Closing Price'] = pd.to_numeric(df['Closing Price'])
df['Open'] = pd.to_numeric(df['Open'])
df['Daily High'] = pd.to_numeric(df['Daily High'])
df['Daily Low'] = pd.to_numeric(df['Daily Low'])
print(df.dtypes)

## Obtaining the mean values of each column
df_NaN = df.dropna()
Open_mean_value = df_NaN['Open'].mean().round(2)
df['Open'] = df['Open'].fillna(Open_mean_value)

Daily_High_mean_value = df_NaN['Daily High'].mean().round(2)
df['Daily High'] = df['Daily High'].fillna(Daily_High_mean_value)

Daily_Low_mean_value = df_NaN['Daily Low'].mean().round(2)
df['Daily Low'] = df['Daily Low'].fillna(Daily_Low_mean_value)

print(df[52:58])



# Exporting the cleaned dataset to a csv file
df.to_csv(r'dataset1.csv', index=False)
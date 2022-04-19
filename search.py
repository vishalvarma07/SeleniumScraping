import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('output1.csv', names=['Title', 'PublishedBy', 'ProductCode', 'Date', 'Price'])

df['Date'].isnull().sum()
df.dropna(inplace=True)

date_df = df['Date'].str.split("-",expand = True)
df = df.drop(['Date'], axis = 1)
df = df.join(date_df)

df.columns = ['Title', 'PublishedBy', 'ProductCode', 'Price', 'Month', 'Day', 'Year']

df['Month'] = df['Month'].astype(int)
df['Day'] = df['Day'].astype(int)
df['Year'] = df['Year'].astype(int)

df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
df.drop(['Year', 'Month', 'Day'], axis = 1, inplace = True)

start_date = input("enter start date(format: yyyy/mm/dd)")
end_date = input("enter end date(format: yyyy/mm/dd)")
date_format = '%Y/%m/%d'
start_date = datetime.datetime.strptime(start_date, date_format)
end_date = datetime.datetime.strptime(end_date, date_format)

required_df = df.loc[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

print(required_df.head())

required_df.to_csv('D:\\required.csv', index=False)

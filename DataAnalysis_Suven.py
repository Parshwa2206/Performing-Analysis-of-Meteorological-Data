import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("weatherHistory.csv")
print(df.head())

tit_req=["Formatted Date","Apparent Temperature (C)","Humidity"]
df=df[tit_req]
print(df.head())

df['Formatted Date']=pd.to_datetime(df['Formatted Date'] , utc=True)
df_1=df.set_index('Formatted Date')
df_1=df_1.resample('MS').mean()
print(df_1.head())
plt.figure(figsize=(14,6))
plt.title("Variation in Apparent Temperature and Humidity with time")
plt.plot(df_1)
df_april=df_1[df_1.index.month==4]
plt.figure(figsize=(14,6))
plt.title("Variation in Apparent Temperature and Humidity with time in April")
plt.plot(df_april)
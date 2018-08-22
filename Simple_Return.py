import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('AAPL.csv')

df_close = df['Close']
close_price = np.array(df_close)

df_date = df['Date']
date = np.array(df_date)

price = []
Anss = [0]
date_temp = []

for i in close_price:
    #print(i)
    price.append(i)

#print(price)

for t in range(1,len(price)):
    ans = ((price[t]/price[t-1])-1)*100
    #print(ans)
    Anss.append(ans)

for i in date:
    temp=i.split("-")
    i=temp[0]+temp[1]+temp[2]
    i=int(i)
    date_temp.append(i)

x = Anss
y = date_temp

print(max(Anss))

plt.plot(df_date,x)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('new.csv')

# Сратегия 1

tst1 = df[['price']][80000:140000]
mn_cost1 = min(tst1['price'])
mx_cost1 = max(tst1['price'])
ind_buy1 = tst1[['price']].idxmin()
ind_sell1 = tst1[['price']].idxmax()
del1 = mx_cost1 - mn_cost1

tst2 = df[['price']][130000:250000]
mn_cost2 = min(tst2['price'])
mx_cost2 = max(tst2['price'])
ind_buy2 = tst2[['price']].idxmin()
ind_sell2 = tst2[['price']].idxmax()

tst = df[['price']]
tst.plot(kind='line', y='price', color='pink')
plt.axvline(x=int(ind_buy2))
plt.axvline(x=int(ind_sell2))
plt.axvline(x=int(ind_buy1))
plt.axvline(x=int(ind_sell1))
plt.grid()
plt.show()
del2 = mx_cost2 - mn_cost2

# Стратегия 2

tst3 = df[['price']][20000:40000]
mn_cost3 = min(tst3['price'])
mx_cost3 = max(tst3['price'])
ind_buy3 = tst3[['price']].idxmin()
ind_sell3 = tst3[['price']].idxmax()
del3 = mx_cost3 - mn_cost3

tst4 = df[['price']][80000:230000]
mn_cost4 = min(tst4['price'])
mx_cost4 = max(tst4['price'])
ind_buy4 = tst4[['price']].idxmin()
ind_sell4 = tst4[['price']].idxmax()
del4 = mx_cost4 - mn_cost4

tst = df[['price']]
tst.plot(kind='line', y='price', color='pink')
plt.axvline(x=int(ind_buy3))
plt.axvline(x=int(ind_sell3))
plt.axvline(x=int(ind_buy4))
plt.axvline(x=int(ind_sell4))
plt.grid()
plt.show()
print('Доходность первой стрегии: ', del1 + del2, '\nДоходность второй стратегии: ', del3 + del4)
print('Дата покупки: ', *df['date'].iloc[ind_buy1], '\nДата продажи: ', *df['date'].iloc[ind_sell1],
      '\nРазница: ', mx_cost1 - mn_cost1)
print('Дата покупки: ', *df['date'].iloc[ind_buy2], '\nДата продажи: ', *df['date'].iloc[ind_sell2],
      '\nРазница: ', mx_cost2 - mn_cost2)
print('\nСуммарная доходность: ', del1+del2)

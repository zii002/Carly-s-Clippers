hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]


total_price = 0

for price in prices:
  total_price += price

print(total_price)
length=len(prices)
print(length)

average_price= total_price/length
print(average_price)
new_prices=[]
for p in prices:
  new_prices.append(p-5)
  print(new_prices)
hlength= len(hairstyles)
print(hlength)
total= []
for i in range(8):
  total.append(last_week[i] * new_prices[i])
print(total)
total_revenue= 0
for i in total:
  total_revenue += i
print('Total Revenue:',total_revenue)
average_daily_revenue= total_revenue/7
print('average daily revenue:', average_daily_revenue)
range_of_new_prices = range(len(new_prices))
print(range_of_new_prices)
cuts_under_30 = [hairstyles[i]for i in range(len(new_prices))
if new_prices[i]< 30]
print(cuts_under_30)






  


 











# Info
hairstyles = ["bouffant", "pixie", "dreadlocks",
              "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Average Price
total_price = 0
for price in prices:
    total_price += price
average_price = round(total_price / len(prices), 2)
print("Average Haircut Price: ${ap}".format(ap=average_price))

# Reducing prices
new_prices = [price - 5 for price in prices]
print(new_prices)

# Finding Revenue
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue: ${tr}".format(tr=total_revenue))
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Finding lowest cost cuts
cuts_under_30 = [hairstyles[i]
                 for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)

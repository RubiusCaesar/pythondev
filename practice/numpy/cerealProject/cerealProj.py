import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')
average_calories = np.mean(calorie_stats)
calorie_stats_sorted = np.sort(calorie_stats)
median_calories = np.median(calorie_stats)
print(average_calories)
print(calorie_stats_sorted)
print(median_calories)
nth_percentile = np.percentile(calorie_stats_sorted, 4)
print(nth_percentile)
more_calories = np.mean(calorie_stats > 60)
print(more_calories)
calorie_std = np.std(calorie_stats)
print(calorie_std)s

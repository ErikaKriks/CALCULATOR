
from random import *
from collections import *
from statistics import mean, stdev

# six roulette wheels -- 18 red, 18 black, 2 green

population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
print(Counter(choice(population) for i in range(6)))

choices(population, k = 6)
n = Counter(choices(["red", "black", "green"], [18, 18, 2], k = 6))
print(n)

# 5 or more from 7 spins of a biased coin
pop = ['heads', "tails"]
wgt = [6, 4]
cumwgt = [0.60, 1.00]

choices(pop, cumwgt)
trial = lambda :  choices(['heads', 'tails'], cumwgt, k = 7).count('heads') >= 5
result = sum(trial() for i in range(100000)) / 100000
print(result)

l = [1, 2, 3, 4, 5, 6]
print(l[0:5:2])
######################################################################################

timings = [7.18, 8.59, 12.24, 7.39, 8.16, 8.68, 6.98,
           8.31, 9.06, 7.06, 7.67, 10.02, 6.87, 9.07]
mt = mean(timings)
print(mt)
print(stdev(timings))

# build 90 % confidence interval
def bootstrap(data):
    return choices(data, k = len(data))

mean(bootstrap(timings))

n = 10000
means = sorted(mean(bootstrap(timings)) for i in range(n))
means[500]
means[-500]
print(f'The observed mean of {mean(timings)}')
print(f'Falls in a 90% confidence interval {means[500]:.1f} to {means[-500]:.1f}')
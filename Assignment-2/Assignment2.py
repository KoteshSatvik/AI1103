import random

n = 0
sum = 0
while n < 1000000 :
    y = 0.5
    x = random.uniform(0,1-y)
    sum = sum + x
    n=n+1


print(sum/1000000)


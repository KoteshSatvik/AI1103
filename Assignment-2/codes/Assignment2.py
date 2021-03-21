import random

n = 0
sum = 0
while n < 1000000 :
    # given
    y = 0.5 
    # given x>0,y>0 and x+y<1 that implies x < 1-y
    # therefore 0 < x < 1-y
    x = random.uniform(0,1-y)
    sum = sum + x
    n=n+1

# The expectation value is 
print(sum/1000000)


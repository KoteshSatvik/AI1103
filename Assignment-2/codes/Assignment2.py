import numpy as np

# Let us consider 1000000 cases.
n = 1000000
# Given y=0.5.
# Given x>0,y>0 and x+y<1 that implies x < 1-y
# therefore 0 < x < 1-y
# implies   0 < x < 1-0.5
# implies   0 < x < 0.5
x = 0.5*np.random.random_sample(n)
sum = np.sum(x)

# The expectation value will be sum/n
exp_value = sum/n
print(exp_value)

import numpy as np

# Let us consider 1000000 cases.
n = 1000000
# Given f(x,y)=a*exp(-2y) and 0<x<y<infinity.
# implies f(x,y) depends only on y and is independant of x.
# As y is given to be 2 (y=2)
# therefore f(x,y) = a*exp(-4), which is a constant
# As 0 < x < 2 and the probability density function is constant,
# then x has equal chance of taking any value between 0 and 2
x = 2*np.random.random_sample(n)
sum = np.sum(x)

# The expectation value will be sum/n
exp_value = sum/n
print(exp_value)

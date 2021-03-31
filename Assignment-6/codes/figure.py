from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import math

n = 100000
_lambda=5.2
x = poisson.rvs(mu=_lambda, size =n )

#let us consider numbers from 0 to 10
m=11
count=[]

for i in range(m):
    count.append(0)

num=0

while num<n:
    if x[num]<11:
        count[x[num]] = count[x[num]]+1
    num=num+1

s_cdf = []
t_cdf = []
t_prob = []
for i in range(m):
    s_cdf.append(0)
    t_cdf.append(0)
    t_prob.append(_lambda**i*math.exp(-_lambda)/math.factorial(i))

i=0
while i<11:
    j=0
    while j<=i:
        s_cdf[i]=s_cdf[i]+count[j]
        j=j+1
    i=i+1
print(count)

i=0
while i<11:
    s_cdf[i] = s_cdf[i]/n
    j=0
    while j<=i:
        t_cdf[i] = t_cdf[i] + t_prob[j]
        j=j+1
    i=i+1

print(s_cdf)
print(t_cdf)

#plotting graph for simulated and theoritical CDFs
cases = ["x=0","x=1","x=2","x=3","x=4","x=5","x=6","x=7","x=8","x=9","x=10"]

x=np.arange(len(cases))
plt.stem(x+0.00,t_cdf, markerfmt='o',use_line_collection=True, basefmt=None, linefmt='orange', label='theoritical cdf')
plt.stem(x+0.25,s_cdf, markerfmt='o',use_line_collection=True, basefmt=None, linefmt='b', label='simulated cdf')
plt.ylabel('F(X)')
plt.xticks(x+0.25/2,[0,1,2,3,4,5,6,7,8,9,10])
plt.legend()
plt.show()
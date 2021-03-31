from scipy.stats import poisson
import seaborn as sb

n = 100000
x = poisson.rvs(mu=5.2, size =n )

sum=0
count = 0
num=0
while num<n:
    sum = sum + x[num]
    if x[num]< 2:
        count = count+1
    num = num+1

print(count/n)
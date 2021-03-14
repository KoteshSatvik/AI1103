from random import randint

# Let X denote the sum of the numbers obtained when two fair dice are rolled.
# When two fair dice are rolled. Let
# x = number obtained on first dice
# y = number obtained on second dice 
# Let us repeat this process 100000 times and 
# find the mean, variance and standard deviation of X.


sum=0
sum_of_squares=0
z=0
while z<100000:
  x=randint(1,6)
  y=randint(1,6)
  sum = sum + x + y
  sum_of_squares = sum_of_squares + ((x+y)**2)

  z=z+1

mean = float(sum)/100000.0
variance = float(sum_of_squares)/100000 - (mean**2)
std_deviation = variance**(0.5)
 
print("The variance of X is : ",variance)
print("The standard deviation of X is : ", std_deviation)


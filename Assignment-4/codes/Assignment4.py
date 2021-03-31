from random import randint

# Let us take the notation:
# head - 0
# tail - 1
# let us consider x is the first time and y is the second time
count_of_Y=0
count_of_N=0
n=0
num = 100000

while (n<num):
  x=1
  y=1
  while (x==1 and y==1):
      x = randint(0,1)
      y = randint(0,1)

      if(x==1 and y==0):
          #print("Y")
          count_of_Y = count_of_Y+1
          break
      
      if(x==0):
          #print("N")
          count_of_N = count_of_N+1
          break
  n=n+1

prob = count_of_Y/num
print("probability of printing Y is ",round(prob,2))


import time
import math
def isPrime1 (num):
    limit=num-1
    for i in range (2, limit+1):
       if num % i == 0: 
          return False
    return True
def isPrime2 (num):
    limit=int(math.sqrt(num))
    for i in range (2, limit+1):
       if num % i == 0: 
          return False
    return True

num = 1000000007
start_time = time.time()
print (isPrime2(num))
print (isPrime1 (num))
end_time = time.time()
elapse_time = end_time - start_time 
print (f" Elapse time: {elapse_time: .2f} seconds")
# start_time = time.time()
# print (isPrime2(num))
# end_time = time.time()
# elapse_time = end_time - start_time 
# print (f" Elapse time: {elapse_time: .2f} seconds")
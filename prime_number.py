import math
from cmath import sqrt

# brute force approach 
def isPrime(n):
    return False if n <=1 else all(n % i != 0 for i in range(2, n))


# smart approach 
def isPrimeSmart(n):
    if n <= 1: 
        return False
    return all(n % i != 0 for i in range(2, math.ceil(math.sqrt(n)))) 


print(isPrime(1))
print(isPrimeSmart(13))
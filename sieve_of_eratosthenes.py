 
  
def SieveOfEratosthenes(num):
    prime = [True for _ in range(num+1)]

# boolean array
    p = 2
    while p**2 <= num:
      
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
          
            # Updating all multiples of p
            for i in range(p**2, num+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            print(p)
  
  
# Driver code
if __name__ == '__main__':
    num = 50
    print("Following are the prime numbers smaller"),
    print("than or equal to", num)
    SieveOfEratosthenes(num)
# coding-interview-preparation
This repository is for code and notes of data structures and algorithms practiced for coding interviews

## Prime Number Test
Definition - A number that is divisible by 1 and itself. 

Brute Force Approach: Time Complexity O(n)

```
for i in range [2, (n-1)]:
    if n % 2 == 0:
    return false

return true
```

Second definition: A number is not prime if it can be written as product of 2 natural numbers greater than 1 and less than the number itself

Let `n` be the number to be checked

1. n = a.b, a is in [2, n-1]
2. We assume that `a` is smaller i.e `a<=b` and therefore `b` can be represented as `n/a`
3. Therefore, `a.b >= a**2` --> `n >= a**2` --> `a <= sqrt(n)`

Smart approach: Time Complexity O(sqrt(n))

```
for i in range [2, sqrt(n)]:
    if n % 2 == 0:
    return false

return true
```
## Prime Factorization

Definition: Prime factorization is dividing a number by prime number multiple times to return 1

Basic Approach: Time Complexity O(n)
```
global f = [], expo = [], len
function primeFact(n):
    d = 2
    while n > 1:
        k = 0
        while n % d == 0:
            n = n/d
            k++
        if k > 0:
            len++
            f[len] = d
            expo[len] = k
        d++
    
```
Smart Approach: Time Complexity O(sqrt(n))

```
global f = [], expo = [], len
function primeFact(n):
    d = 2
    while n > 1 && d*d <=n:
        k = 0
        while n % d == 0:
            n = n/d
            k++ 
        if k > 0:
            len++
            f[len] = d
            expo[len] = k
        d++

    if n > 1:
    len++
    f[len] = n
    
```

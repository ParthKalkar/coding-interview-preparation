n = 0
arr = []
arr1 = []

def primeFact(n):
    d = 2
    while d ** 2 <= n and n > 1:
        k = 0
        while n % d == 0:
            k = k + 1
            n = n // d

        if k > 0:
            arr.append(d)
            arr1.append(k)
        d += 1
        
    if n > 1:
        arr.append(n)
        arr1.append(1)

    return arr, arr1

a, b = primeFact(1331)
print(a, b)
def factors(n):
    results = [] 
    for k in range(1, n+1):
        if n%k == 0:
            results.append(k)
    return results 

def factors_g(n): 
    for k in range(1,n+1): 
        if n%k == 0: 
            yield k 

def fast_factors(n): 
    k = 1
    while k*k < n: 
        if n % k == 0:
            yield k 
            yield n//k
        k+=1
    if k*k == n: 
        yield k 

def fib_g():
    a = 0 
    b = 1
    while True: 
        yield a
        future = a + b 
        a = b 
        b = future 


'''
R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''
def multiple(n,m): 
    return m % n == 0

assert multiple(2,1) == False 
assert multiple(2,2) == True  
assert multiple(3,1) == False  
assert multiple(3,2) == False  
assert multiple(3,3) == True 

assert multiple(4,1) == False 
assert multiple(4,2) == False  
assert multiple(4,3) == False  
assert multiple(4,4) == True  
assert multiple(1,4) == True  
assert multiple(2,4) == True  
assert multiple(3,4) == False  

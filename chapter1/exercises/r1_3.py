'''
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''
def minmax(seq): 
    mn = None  
    mx = None  
    for v in seq: 
        if mn == None: 
            mn = v 
        if mx == None: 
            mx = v

        if v < mn: 
            mn = v 
        if v > mx: 
            mx = v 

    return (mn,mx)

assert minmax([1,1]) == (1,1)
assert minmax([2,1]) == (1,2)
assert minmax([0,-1]) == (-1,0)
assert minmax([0,1,2,3]) == (0,3)
assert minmax([-1_000, 2, 5, 3, 1_000, 10, 125]) == (-1_000,1_000)

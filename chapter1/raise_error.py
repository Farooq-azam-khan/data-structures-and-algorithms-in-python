import math 
import collections

def sqrt(x): 
    if not isinstance(x, (int,float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative') 
    return math.sqrt(x) 

def sum(values): 
    if not isinstance(values, collections.abc.Iterable):
        raise TypeError('parameter must be an iterable type')
    total = 0 
    for v in values: 
        if not isinstance(v, (int,float)): 
            raise TypeError('element must be numeric')
        total += v 
    return total 


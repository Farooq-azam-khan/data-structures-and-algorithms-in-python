'''
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
'''

def diff_seq(seq): 
    return len(set(seq)) == len(seq)

assert diff_seq([1,2,3]) == True 
assert diff_seq([3,3]) == False
assert diff_seq(['one', 'two', 'three']) == True 
assert diff_seq(['three', 'three']) == False
assert diff_seq([3, 'three']) == True 


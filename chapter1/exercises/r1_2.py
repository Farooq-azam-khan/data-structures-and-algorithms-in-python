'''
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''
def is_even(k:int):
    last_digit = str(k)[-1]

    return (last_digit == '0' or \
            last_digit == '2' or \
            last_digit == '4' or  \
            last_digit == '6' or  \
            last_digit == '8')


assert is_even(0) == True 
assert is_even(1) == False  
assert is_even(2) == True 
assert is_even(3) == False  
assert is_even(4) == True 
assert is_even(5) == False  
assert is_even(6) == True  
assert is_even(7) == False  
assert is_even(8) == True 
assert is_even(9) == False  
assert is_even(10) == True
assert is_even(1_295_624) == True
assert is_even(1_295_622) == True


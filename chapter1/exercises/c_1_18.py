'''
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
'''
'''
index | value | formula  
0     | 0     | 0*(1+0)
1     | 2     | 1*(1+1)
2     | 6     | 2*(1+2)
3     | 12    | 3*(1+3)
4     | 20    | 4*(1+4)
5     | 30    | 5*(1+5)
6     | 42    | 6*(1+6)
7     | 56    | 7*(1+7)
8     | 72    | 8*(1+8)
9     | 90    | 9*(1+9)
general form  | T_n = i * (1+i)
'''
true_ans = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
my_ans = [i*(1+i) for i in range(0, 9+1)] 

print('Is Correct list:', my_ans == true_ans) 
print(my_ans) 

'''
Exercise 25
Your task is to swap the values of x and y. 

INPUT: int
x = 3 y = 2
OUTPUT: int
x = 2 y = 3

use temporary variable, not tuple method

'''

x = int(input("first input x ="))
y = int(input("second input y = "))

temp = x
x = y
y = temp

print("x = ", x)
print("y = " , y)

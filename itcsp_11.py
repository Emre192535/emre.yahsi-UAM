'''
Exercise 11
Write a program that will check whether the given number is even or odd
INPUT: int
use input() function
text to appear:
'Enter the integer number'

OUTPUT: str
'Even'
or
'Odd'

'''

number = int(input("enter a number"))
if(number%2 == 0):
    print("even")
else:
    print("odd")
'''
Exercise 17
For any entered string. Write a program that will reverse the order of the letters and print to the console.
e.g., for "Hello world", printed result should be 'dlrow olleH’
Typing in an "exit" should break the loop end exit the program
INPUT: str
OUTPUT: str

Use while loop, input() 

'''

while(True):
    string = input("enter a string ")
    print("type exit to exit ")
    a= 1
    for i in string:
        print(string[len(string)-a])
        a +=1

    if string=='exit':
        break
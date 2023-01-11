'''
Exercise 21
For any entered string. Write a program that will reverse the order of the letters and print to the console.
e.g., for "Hello world", printed result should be 'dlrow olleH
Typing in an "exit" should break the loop end exit the program
INPUT: str
OUTPUT: str

Use while loop, input(), use lists

'''

while True:
    revList = []
    names = input("Please enter a word")
    i = 1
    if names == "exit":
        break
    for element in names:
        revList.append(names[len(names)-i])
        i += 1
    
    print(revList)
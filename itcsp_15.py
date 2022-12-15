'''
Exercise 15
Write a program that counts vowels in a string
The program should implement the possibility for the user to enter any word.

INPUT: str
OUTPUT: str

Use input() function
vowels = 'aeiou'

The exemplary input:
Enter a word ... 

The exemplary output in  terminal should be:
You have 6 vowels in a word "Appalachicola"
Tests:
VOWELS -> 2 vowels
vowels -> 2 vowels
Appalachicola -> 6 vowels

'''
vowels = 'aeiou'
word = input("write a word : ")
count = 0 
for i in word:
    if i in vowels:
        count +=1 

print(count)

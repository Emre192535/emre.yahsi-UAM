'''
Exercise 31 (modify exercise 15)
Write a program that counts vowels in a string
The program should implement the possibility for the user to enter any word.

INPUT: str
OUTPUT: str

DEFINE YOUR OWN FUNCTION:
    count_vowels(text:str)->int
    remember about docstring

Finally
use input() function to enter text
invoke count_vowels function
use f-string formatting together with print function

vowels = 'aeiou'

The exemplary input:
Enter a word ... 

The exemplary output in  terminal should be:
You have 6 vowels in the word "Appalachicola"
Tests:
VOWELS -> 2 vowels
vowels -> 2 vowels
Appalachicola -> 6 vowels

'''

def count_vowels(str):
    vowels = 'aeiou'

    count = 0 
    for i in word:
       if i in vowels:
           count +=1 
    
    print(count)

 
word = input("write a word : ")
count_vowels(word)
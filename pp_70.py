'''
Exercise 70, file "pp_70.py"
LEARNING DICTIONARY COMPREHESION
Write a program that will print to display a list of tuples that will consist of the most frequent character in the sentence / sentences and it's frequency, sorted in a descending order.
In order to complete the task
1. define a function
def most_freq_character(sentence):
2. As a data structure use a dictionary
3. In your analize, don't use spaces, coma, dots
4. use count() method of string class to count characters
For testing purposes you can use
sentence = "The robbed that smiles, steals something from the thief."
Expected result:
[('t', 7), ('e', 7), ('h', 5), ('s', 5), ('o', 3), ('m', 3), ('i', 3), ('r', 2), ('b', 2), ('a', 2), ('l', 2), ('f', 2), ('d', 1), ('n', 1), ('g', 1)]
'''

def most_freq_character(sentence):
    # Remove all whitespace, commas, and dots from the sentence
    sentence = sentence.replace(" ", "").replace(",", "").replace(".", "")
    
    # Create a dictionary comprehension to count the frequency of each character in the sentence
    characters_freq = {char: sentence.count(char) for char in sentence}
    
    # Sort the dictionary by value in descending order and store it in a list of tuples
    sorted_characters_freq = sorted(characters_freq.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_characters_freq

sentence = "The robbed that smiles, steals something from the thief."
result = most_freq_character(sentence)
print(result)
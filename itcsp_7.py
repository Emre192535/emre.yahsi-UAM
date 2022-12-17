'''
Exercise 07
Create a string made of the first, middle and last character and print it to the terminal

Expected results
text = 'abcdefg'  # expected result: adg
text = 'abcdef'  # expected result adf

Hints:
Use string indexing to get the character present at the given index
Get the index of the middle character by dividing string length by 2
Function that returns string length:
l= len(text)

'''

text = "Emreyahsi"
first = text[0]
middle = text[int(len(text)/2)]
last = text[len(text)-1]

result = first+middle+last

print(result)
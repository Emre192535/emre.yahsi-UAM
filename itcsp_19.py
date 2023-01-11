'''
Exercise 19
There is a list
hashtags = ['spring','summer','winter']
Connect these element with "#". Add this sign also at the beginning.
Print the result to the terminal
INPUT: list
OUTPUT: str
Expected result: #spring#summer#winter
'''
string = "  "
hashtags = ['spring','summer','winter']
for elements in hashtags:
    string = string + "#" + elements

print(string)
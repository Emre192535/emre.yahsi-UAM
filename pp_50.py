'''
Write a program that will filter a list of tuple.
In order to do it, a list of tuples is given (for testing purposes)
L1 = [
…
]
In your program, write a function that will return a filtered list of tuples.def filter_list(filtering_criterion, items):
# input: list of tuples
# return: filtered list of tuples
# Use loop
return price_filtered
For testing purposes, assume filter criteria : all elements that has a price greater than 15
'''

def filter_list(filtering_criterion, items):
    price_filtered = []
    for item in items:
        if item[1] > filtering_criterion:
            price_filtered.append(item)
    return price_filtered

L1 = [('apple', 10), ('banana', 20), ('orange', 15), ('pear', 30), ('kiwi', 5)]

filtered_list = filter_list(15, L1)

print(filtered_list)
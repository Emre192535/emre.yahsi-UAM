shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ....'

def get_longest_word(text: str) -> tuple[str, int]:
    # remove commas and periods from the text
    text = text.replace(',', '').replace('.', '')
    # get a list of all words in the text
    words = text.split()
    # use dictionary comprehension to get word:length pairs
    word_lengths = {word: len(word) for word in words}
    # sort the word:length pairs by length in descending order
    sorted_word_lengths = sorted(word_lengths.items(), key=lambda x: x[1], reverse=True)
    # return the longest word and its length
    return sorted_word_lengths[0]

# call the function with the given text
longest_word, length = get_longest_word(shakespeare)

# print the result
print(f"The longest word is '{longest_word}' with the length {length} characters.")


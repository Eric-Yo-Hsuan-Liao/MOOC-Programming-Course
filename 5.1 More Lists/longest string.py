

def longest(strings: list):
    longest = strings[0]
    for word in strings:
        length = len(word)
        if length > len(longest):
            longest = word
    return longest

strings = ['hi', 'hiya', 'hello', 'howdydoody', 'hi there']
print(longest(strings))
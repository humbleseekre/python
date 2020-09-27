'''
Challenge: Write a python function to sort the words in a string

input: String of words, separated by spaces => 'banana ORANGE apple'
output: string of words, sorted alphabetically => 'apple banana ORANGE'
'''

def sort_words(input):
    words = input.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)

print sort_words('banana ORANGE apple')


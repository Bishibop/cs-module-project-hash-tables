import random
import re
from functools import partial

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

    word_arr = words.split()
    word_dict = {}

    for i, word in enumerate(word_arr):
        if i+1 != len(word_arr):
            next_word = word_arr[i+1]
            if word in word_dict:
                word_dict[word].append(next_word)
            else:
                word_dict[word] = [next_word]

    start_words = [word for word in word_arr if re.match(r'([A-Z]|")', word)]

    for i in range(5):
        current_word = random.choice(start_words)
        sentence = []
        if re.match(r'"', current_word):
            stop_match = partial(re.search, r'[\.\?!]"$')
        else:
            stop_match = partial(re.search, r'[\.\?!]$')
        while not stop_match(current_word):
            sentence.append(current_word)
            current_word = random.choice(word_dict[current_word])
        sentence.append(current_word)
        print(' '.join(sentence) + '\n')


# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here

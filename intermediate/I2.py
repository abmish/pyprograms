"""
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new
word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at
http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same
characters that contain the most words in them.
"""

from collections import defaultdict

def load_words(filename):
    with open(filename) as f:
        for word in f:
            yield word.rstrip()

def get_anagrams(source):
    d = defaultdict(list)
    for word in source:
        key = "".join(sorted(word))
        d[key].append(word)
    return d

def print_anagrams(word_source):
    d = get_anagrams(word_source)
    for key, anagrams in d.iteritems():
        if len(anagrams) > 1:
            print(key, anagrams)

def get_max_anagram_set(word_source):
    max_len = 0
    max_anagram = None
    d = get_anagrams(word_source)
    for key, anagrams in d.iteritems():
        if len(anagrams) > max_len:
            max_len = len(anagrams)
            max_anagram = anagrams
    return max_anagram

word_source = load_words('I2_unixdict.txt')
# print_anagrams(word_source)
print get_max_anagram_set(word_source)
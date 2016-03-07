# -*- coding: utf-8 -*-
"""
A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence
splitting includes (but isn't limited to) the following rules:
Sentence boundaries occur at one of "." (periods), "?" or "!", except that
    Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
    Periods followed by a digit with no intervening whitespace are not sentence boundaries.
    Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not  sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
    Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example,  www.aptex.com, or e.g).
    Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.

Your task here is to write a program that given the name of a text file is able to write its content with each sentence
on a separate line. Test your program with the following short text: Mr. Smith bought cheapsite.com for 1.5 million
dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well,
with a probability of .9 it isn't. The result should be:

Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind?
Adam Jones Jr. thinks he didn't.
In any case, this isn't true...
Well, with a probability of .9 it isn't.
"""

abbreviations = {'Dr.': 'Doctor', 'dr.': 'doctor',
                 'Mr.': 'Mister', 'mr.': 'mister', 'Mrs.': 'Mistress', 'mrs.': 'mistress', 'Ms.': 'Miss', 'ms.': 'miss',
                 'bro.': 'brother', 'bro': 'brother',
                 'Jr.': 'Junior', 'jr.': 'junior', 'Sr.': 'Senior', 'sr.': 'senior',
                 'i.e.': 'for example', 'e.g.': 'for example', 'vs.': 'versus'}
terminators = ['.', '!', '?']
wrappers = ['"', "'", ')', ']', '}']


def find_sentences(paragraph):
   end = True
   sentences = []
   while end > -1:
       end = find_sentence_end(paragraph)
       if end > -1:
           sentences.append(paragraph[end:].strip())
           paragraph = paragraph[:end]
   sentences.append(paragraph)
   sentences.reverse()
   return sentences


def find_sentence_end(paragraph):
    [possible_endings, contraction_locations] = [[], []]
    contractions = abbreviations.keys()
    sentence_terminators = terminators + [terminator + wrapper for wrapper in wrappers for terminator in terminators]

    for sentence_terminator in sentence_terminators:
        t_indices = list(find_all(paragraph, sentence_terminator))
        possible_endings.extend(([] if not len(t_indices) else [[i, len(sentence_terminator)] for i in t_indices]))

    for contraction in contractions:
        c_indices = list(find_all(paragraph, contraction))
        contraction_locations.extend(([] if not len(c_indices) else [i + len(contraction) for i in c_indices]))

    possible_endings = [pe for pe in possible_endings if pe[0] + pe[1] not in contraction_locations]

    if len(paragraph) in [pe[0] + pe[1] for pe in possible_endings]:
        max_end_start = max([pe[0] for pe in possible_endings])
        possible_endings = [pe for pe in possible_endings if pe[0] != max_end_start]
    possible_endings = [pe[0] + pe[1] for pe in possible_endings if sum(pe) > len(paragraph) or (sum(pe) < len(paragraph) and paragraph[sum(pe)] == ' ')]

    end = (-1 if not len(possible_endings) else max(possible_endings))

    return end


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)

with open('I1_data.txt', 'r') as txt_file:
    file_data = txt_file.read()

print "\n".join(find_sentences(file_data))
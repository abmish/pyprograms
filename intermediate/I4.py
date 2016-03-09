"""
but that word must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated.
A certain children's game involves starting with a word in a particular category. Each participant in turn says a word,
If an opponent cannot give a word in the category, they fall out of the game. For example, with "animals" as the category,
Child 1: dog
Child 2: goldfish
Child 1: hippopotamus
Child 2: snake
...

Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names (extracted from
Wikipedia's list of Pokemon) and generate the/a sequence with the highest possible number of Pokemon names where the
subsequent name starts with the final letter of the preceding name. No Pokemon name is to be repeated.

audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask
"""

from collections import defaultdict
def order_words(words):
    by_first = defaultdict(set)
    for word in words:
        by_first[word[0]].add(word)
    return by_first

def link_first(by_first, so_far):
    assert so_far
    match = so_far[-1][-1]
    options = by_first[match] - set(so_far)
    if not options:
        return so_far
    else:
        alternatives = (link_first(by_first, list(so_far) + [word]) for word in options)
        o_max = max(alternatives, key=len)
        return o_max

def arrange_words(words):
    by_first = order_words(words)
    return max( (link_first(by_first, [word]) for word in words), key= len)

pokemons = ['audino', 'bagon', 'baltoy', 'banette', 'bidoof', 'braviary', 'bronzor', 'carracosta', 'charmeleon',
            'cresselia', 'croagunk', 'darmanitan', 'deino', 'emboar', 'emolga', 'exeggcute', 'gabite', 'girafarig',
            'gulpin', 'haxorus', 'heatmor', 'heatran', 'ivysaur', 'jellicent', 'jumpluff', 'kangaskhan', 'kricketune',
            'landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone', 'machamp', 'magnezone', 'mamoswine', 'nosepass',
            'petilil', 'pidgeotto', 'pikachu', 'pinsir', 'poliwrath', 'poochyena', 'porygon2', 'porygonz', 'registeel',
            'relicanth', 'remoraid', 'rufflet', 'sableye', 'scolipede', 'scrafty', 'seaking', 'sealeo', 'silcoon',
            'simisear', 'snivy', 'snorlax', 'spoink', 'starly', 'tirtouga', 'trapinch', 'treecko', 'tyrogue', 'vigoroth',
            'vulpix', 'wailord', 'wartortle', 'whismur', 'wingull', 'yamask']

arrangement = arrange_words(pokemons)
for i in range(0, len(arrangement), 8):
    print ' '.join(arrangement[i:i+8])
print(len(arrangement))

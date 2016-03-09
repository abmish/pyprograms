1)  
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
  
2)  
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new  
word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at  
http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same  
characters that contain the most words in them.  
  
3)  
For two segments of integer [l1, r1] and [l2, r2]. How many pair (x, y) which l1 <= x <= r1 and l2 <= y <= r2 where x * y divisible by p.  
Input  
The first line is integer p (1 <= p <= 10^9)  
Second line includes l1, r1 separated by a space (1 <= l1 <= r1 <= 10^9).  
Third line includes l2, r2 separated by a space (1 <= l2 <= r2 <= 10^9).  
  
4)  
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
  



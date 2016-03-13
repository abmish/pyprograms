"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
words = [
    (1,'one',''), (2,'two',''), (3,'three',''), (4,'four',''), (5,'five',''),
    (6,'six',''), (7,'seven',''), (8,'eight',''), (9,'nine',''), (10,'ten',''),
    (11,'eleven',''), (12,'twelve',''), (13,'thirteen',''), (14,'fourteen',''), (15,'fifteen',''),
    (16,'sixteen',''), (17,'seventeen',''), (18,'eighteen',''), (19,'nineteen',''), (20,'twenty',''),
    (30,'thirty',''), (40,'forty',''), (50,'fifty',''), (60,'sixty',''), (70,'seventy',''),
    (80,'eighty',''), (90,'ninety',''), (100,'hundred','and'), (1000,'thousand','and'),
]

words.reverse()

def spelling(num, words):
    spell = []
    while num >=1:
        for digit in words:
            if digit[0] <= num:
                div = num / digit[0]
                num = num % digit[0]
                if digit[2]: spell.append(' '.join(spelling(div, words)))
                spell.append(digit[1])
                if digit[2] and num : spell.append(digit[2])
                break
    return spell

print sum(len(word) for num in xrange(1,1001) for word in spelling(num, words))
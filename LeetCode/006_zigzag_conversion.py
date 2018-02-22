"""
url: https://leetcode.com/problems/zigzag-conversion/description/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""


import itertools


def convert(s, numRows):
    s_len = len(s);
    out = "";
    if numRows == 1 or s_len in [0, 1, 2]:
        return s

    if numRows == 2:
        out = [s[0::2], s[1::2]];
        return ''.join(list(itertools.chain(*out)));

    for i in range(numRows):
        k = i;
        for j in range(s_len):
            if k >= s_len:
                break;
            out += s[k];
            k += 2 * (numRows - i - 1) if ((i == 0 or (j % 2 == 0)) and (i != numRows - 1)) else 2 * i;
    return out


print(convert('PAYPALISHIRING', 3))
print(convert('ABC', 4))
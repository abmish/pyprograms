"""
url: https://leetcode.com/problems/integer-to-roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

"""
def intToRoman1(num):  # runtime 140 ms on Leetcode
    """
    :type num: int
    :rtype: str
    """

    roman_numerals = ["","I","II","III","IV","V","VI","VII","VIII","IX",
                          "","X","XX","XXX","XL","L","LX","LXX","LXXX","XC",
                          "","C","CC","CCC","CD","D","DC","DCC","DCCC","CM",
                          "","M","MM","MMM","MMMM"]
    return roman_numerals[ num // 1000 + 30] + roman_numerals[(num // 100) % 10 + 20] + roman_numerals[(num // 10) % 10 + 10] + roman_numerals[num % 10]


def intToRoman2(num):  # runtime 116ms on Leetcode
    M = ["", "M", "MM", "MMM"];
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
    return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10];


print(intToRoman1(1))
print(intToRoman1(5))
print(intToRoman1(15))

print(intToRoman2(1))
print(intToRoman2(5))
print(intToRoman2(15))
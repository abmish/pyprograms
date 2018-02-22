"""
url: https://leetcode.com/problems/regular-expression-matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

"""


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    if p == '.*':
        return True

    if '.' not in p and '*' not in p:
        return True if p == s else False

    prev = [False, True]
    for j in range(len(p)):
        prev.append(p[j] == '*' and prev[j])

    for i in range(len(s)):
        curr = [False, False]
        for j in range(len(p)):
            if p[j] == '*':
                curr.append(curr[j] or curr[j + 1] or (prev[j + 2] and p[j - 1] in (s[i], '.')))
            else:
                curr.append(prev[j + 1] and p[j] in (s[i], '.'))
        prev = curr
    return prev[-1]

print("aa","a")
print(isMatch("aa","a"))
print("aa","aa")
print(isMatch("aa","aa"))
print("aaa","aa")
print(isMatch("aaa","aa"))
print("aa", "a*")
print(isMatch("aa", "a*"))
print("aa", ".*")
print(isMatch("aa", ".*"))
print("ab", ".*")
print(isMatch("ab", ".*"))
print("aab", "c*a*b")
print(isMatch("aab", "c*a*b"))
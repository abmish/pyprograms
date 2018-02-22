"""
url: https://leetcode.com/problems/longest-substring-without-repeating-characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):  # First submission on LeetCode: run time 80 ms, beats 100% submissions so not trying again
        """
        :type s: str
        :rtype: int
        """
        length = len(s);
        if length in [0, 1]:
            return length;
        current_length = 1;
        max_length = 1;

        visited = [-1] * 256;
        visited[ord(s[0])] = 0;

        for counter in range(1, length):
            previous_index = visited[ord(s[counter])];
            if previous_index == -1 or (counter - current_length > previous_index):
                current_length = current_length + 1;
            else:
                if current_length > max_length:
                    max_length = current_length;
                current_length = counter - previous_index;
            visited[ord(s[counter])] = counter;

        if current_length > max_length:
            max_length = current_length;

        return max_length;
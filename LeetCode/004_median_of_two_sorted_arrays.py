"""
url: https://leetcode.com/problems/median-of-two-sorted-arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:

    def findMedianSortedArrays(self, nums1, nums2):  # run time 100 ms; best on LeetCode
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def median_single_array(inlist, lenlist):
            if lenlist == 0:
                return -1
            if lenlist % 2 == 0:
                return (inlist[lenlist / 2] + inlist[1 + lenlist / 2]) / 2
            return inlist[lenlist / 2]

        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, m, nums2, n = nums2, n, nums1, m
        if n == 0:
            return median_single_array(nums2, n) / 1.0

        min_len, max_len, half_len = 0, m, (m + n + 1) // 2
        while min_len <= max_len:
            i = (min_len + max_len) // 2
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                # i is small, increase
                min_len = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is big, decrease
                max_len = i - 1
            else:  # i is right
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) & 1 == 1:
                    return max_of_left / 1.0

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

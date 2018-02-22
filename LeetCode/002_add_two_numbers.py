"""
url: https://leetcode.com/problems/add-two-numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def add_two_numbers1(self, l1, l2):  # First submission on LeetCode: run time 235 ms
        str1, str2 = '', ''
        while l1.next:
            str1 = str(l1.val) + str1
            l1 = l1.next
        str1 = str(l1.val) + str1
        while l2.next:
            str2 = str(l2.val) + str2
            l2 = l2.next
        str2 = str(l2.val) + str2
        output = int(str1) + int(str2)
        output = str(output)
        outl = ListNode(0)
        for o in output:
            n = ListNode(o)
            outl.next, n.next = n, outl.next
        return outl.next

    def add_two_numbers2(self, l1, l2):  # Second submission on LeetCode: run time 193 ms
        d_head = ListNode(0)
        c = d_head
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = carry + x + y
            carry = sum // 10
            c.next = ListNode(sum % 10)
            c = c.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            c.next = ListNode(carry)
        return d_head.next

    def add_two_numbers3(self, l1, l2):  # Third submission on LeetCode: run time 116 ms
        carry = 0;
        res = n = ListNode(0);
        while l1 or l2 or carry:
            if l1:
                carry = carry + l1.val;
                l1 = l1.next;
            if l2:
                carry = carry + l2.val;
                l2 = l2.next;
            carry, val = divmod(carry, 10);
            n.next = n = ListNode(val);
        return res.next;

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.add_two_numbers3(l1, l2)

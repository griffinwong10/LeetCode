# Griffin Wong
# 04/25/2020

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""

class Solution:
    def reverse(self, x: int) -> int:
        l2 = [str(d) for d in reversed(str(x))]
        return (int("".join(l2)))
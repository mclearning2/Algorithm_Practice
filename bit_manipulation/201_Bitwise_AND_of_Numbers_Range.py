'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        for i in range(32):
            a = 1 << i
            b = 1 << (i+1)
            if a <= m < b and a <= n < b:
                for j in range(m, n+1):
                    m = m & j
                return m
                
        return 0

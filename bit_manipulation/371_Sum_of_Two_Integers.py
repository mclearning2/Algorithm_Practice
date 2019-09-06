'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''
# Full Adder

class Solution:
    def getSum(self, a: int, b: int) -> int:
        answer = 0
        s = 0
        c = 0
        for i in range(32):
            a1 = ((a >> i) & 1)
            b1 = ((b >> i) & 1)
            xor = a1 ^ b1
            s = xor ^ c
            and1 = a1 & b1
            and2 = xor & c
            c = and1 ^ and2
            
            answer = answer | (s << i)
        if answer & (2 ** 31):
            
            return -((~answer +1) % 2**31)
        else:
            return answer

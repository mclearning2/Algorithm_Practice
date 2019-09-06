'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        answer = 0
        memory = list(range(n))
        memory[:2] = None, None
        for i in range(2, n):
            if memory[i]:
                answer += 1
                for j in range(i, n, i):
                    memory[j] = None
        return answer
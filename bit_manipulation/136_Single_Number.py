```
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
```
# Solution 1. list 
# time complexity : O(N^2) 
# space complexity : O(N)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = []
        for n in nums:
            if n in l:
                l.remove(n)
            else:
                l.append(n)
        return l[0]
        
# Solution 2. Manipulation
# time complexity: O(N)
# space complexity: O(1)

from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums)

'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''
# Solution 1. Dynamic Programming
# Sorted function use a Tim sort algorithm.
# Time : O(N logN)
# Space : O(N)

from math import floor
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        return sorted(nums)[floor(l/2) if l % 2 else l//2-1]
        
# Solution 2. Bit Manipulation
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        answer = 0
        for i in range(32):
            cnt = 0
            for n in nums:
                cnt += n >> i & 1
            if cnt >= len(nums) / 2:
                answer += 1 << i
        
        # For negative
        if answer & i << 31:
            return -(answer % (2 ** 32 - 1) + 1)
        else:
            return answer

# Solution 3. Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        cnt = 1
        for n in nums[1:]:
            majority = n if cnt == 0 else majority
            cnt += majority == n
        return majority

''' 78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''
# Dynamic Programming
# [] -> []
# [1] -> [], [1]
# [1,2] -> [], [1], [2], [1,2]
# [1,2,3] -> [], [1], [2], [1,2], [3], [3,1], [3,2], [3,1,2]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for i in nums:
            for n in range(len(answer)):
                answer.append(answer[n] + [i])
        return answer
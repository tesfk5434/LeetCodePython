#https://leetcode.com/problems/two-sum/description/

#Status: Completed
#Time Complexity: O(n), Beats 100%
#Space Complexity: O(n), Beats 50%
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, val in enumerate(nums):
            if target-val in table:
                return [i, table[target-val]]
            table[val] = i
        return None
        
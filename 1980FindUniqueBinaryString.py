# https://leetcode.com/problems/find-unique-binary-string/submissions/1549172307/

#Status: Completed
#Time Complexity: O(n), Beats 100%
#Space Complexity: O(n), Beats 98.15%
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        string = []
        for i in range(len(nums)):
            if nums[i][i] =="0":
                string.append("1")
            else:
                string.append("0")
        return "".join(string)
        
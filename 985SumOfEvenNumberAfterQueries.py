# https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

#Status: Completed
#Time Complexity: O(n), Beats 75.09%
#Space Complexity: O(n), Beats 63.51%


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        prefixSum = sum(x for x in nums if x%2==0)
        ans=[]
        for (val, index) in queries:
            originalNum = nums[index]
            nums[index] += val
            prefixSum -= originalNum if originalNum%2==0 else 0
            prefixSum += nums[index] if nums[index]%2==0 else 0
            ans.append(prefixSum)
        return ans

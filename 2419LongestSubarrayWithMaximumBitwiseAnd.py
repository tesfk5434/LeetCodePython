# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

#Status: Completed
#Time Complexity: O(n), Beats 89.27%
#Space Complexity: O(n), Beats 44.64%

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum, count,ans = max(nums), 0,0
        for num in nums:
            if num != maximum:
                ans=max(ans,count)
                count=0
            else:
                count+=1
        return max(ans,count)
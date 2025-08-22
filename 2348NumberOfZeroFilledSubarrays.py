class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        p, ans, size = 0, 0, 0
        while p<len(nums):
            while p<len(nums) and nums[p]==0:
                size+=1
                p+=1
            if size!=0:
                ans += size*(size+1)//2
                size=0
            p+=1
        return ans
#https://leetcode.com/problems/bitwise-ors-of-subarrays/?envType=daily-question&envId=Invalid%20Date

#Status: Completed
#Time Complexity: O(n), Beats 86.31%
#Space Complexity: O(n), Beats 74.40%



class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        lastSet = set([])
        totalSet = set([])
        for i in range(0,len(arr)):
            num = arr[i]
            newSet = set([num])
            for bitwiseOr in lastSet:
                newSet.add(bitwiseOr | num)
            totalSet |= newSet
            lastSet = newSet
        return len(totalSet)

                

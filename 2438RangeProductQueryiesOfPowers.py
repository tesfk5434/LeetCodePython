# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

#Status: Completed
#Time Complexity: O(m + n), Beats 70.19%
#Space Complexity: O(n), Beats 41.24%

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powerOfTwo = 1
        powers = []
        ans = []
        while powerOfTwo * 2 <= n:
            powerOfTwo *= 2
        while n>0:
            if powerOfTwo <= n:
                n -= powerOfTwo
                powers.append(powerOfTwo)
            powerOfTwo //= 2
        powers.reverse()
        prefix = []
        product = 1
        for power in powers:
            prefix.append(product)
            product *= power
        prefix.append(product)
        for l, r in queries:
            ans.append((prefix[r+1]//prefix[l]) % (10**9 + 7))
        return ans

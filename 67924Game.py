# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

#Status: Completed
#Time Complexity: O(1), Beats 92.78%
#Space Complexity: O(1), Beats 65.78%
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        globalBoolean = [False]
        def combineTerms(cards):
            if len(cards)==1 or globalBoolean[0] == True:
                if abs(24 - cards[0])<0.0000001:
                    globalBoolean[0] = True
                return
            for i in range(len(cards)):
                for j in range(i+1, len(cards)):
                    arr = [cards[i]+cards[j]] + [cards[k] for k in range(len(cards)) if (k != j) and (k!=i)]
                    combineTerms(arr)
                    arr[0] = cards[i]-cards[j]
                    combineTerms(arr)
                    arr[0]= cards[j]-cards[i]
                    combineTerms(arr)
                    arr[0] = cards[i] * cards[j]
                    combineTerms(arr)
                    if cards[j]!=0:
                        arr[0] = cards[i]/cards[j]
                        combineTerms(arr)
                    if cards[i]!=0:
                        arr[0] = cards[j]/cards[i]
                        combineTerms(arr)
        combineTerms(nums)
        return globalBoolean[0]

                    



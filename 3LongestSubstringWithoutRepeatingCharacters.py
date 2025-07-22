#https://leetcode.com/problems/two-sum/description/

#Status: Completed
#Time Complexity: O(n), Beats 97.92%
#Space Complexity: O(n), Beats 53.10%

##iterate over the string, storing each character. Once finding a repeated character, then remove all elements before the previous occurence character
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, count = 0 , 0, 0
        elements = set([])
        while r<len(s):
            if s[r] in elements:
                while s[l] !=s[r]:
                    elements.remove(s[l])
                    l+=1
                l+=1
            else:
                elements.add(s[r])
                count = max(len(elements), count)
            r+=1
        return count
                

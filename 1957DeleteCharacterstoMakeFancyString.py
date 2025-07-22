# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

#Status: Completed
#Time Complexity: O(n), Beats 98.42%
#Space Complexity: O(n), Beats 12.85%

class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = [s[0]]
        lastChar = s[0]
        count=1
        for char in s[1:]:
            if lastChar == char and count==1:
                ans.append(char)
                count+=1
            elif lastChar != char:
                ans.append(char)
                lastChar = char
                count=1
        return ''.join(ans)

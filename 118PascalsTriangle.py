# https://leetcode.com/problems/pascals-triangle/

#Status: Completed
#Time Complexity: O(n), Beats 100.00%
#Space Complexity: O(n), Beats 16.22%


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for row in range(2, numRows+1):
            newRow = [1]
            for index in range(1, row-1):
                newRow.append(ans[-1][index]+ ans[-1][index-1])
            newRow.append(1)
            ans.append(newRow)
        return ans
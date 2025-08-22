class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        dp = [[0] * (len(mat[0]) + 1) for _ in range(len(mat)+1)]
        ans = 0
        for row in range(1,len(mat)+1):
            for col in range(1, len(mat[0])+1):
                dp[row][col] = dp[row-1][col] + 1 if mat[row-1][col-1] == 1 else 0
                height = dp[row][col]
                p = col
                while height!=0 and 0<p:
                    height = min(height, dp[row][p])
                    ans += height
                    p-=1
        return ans
                





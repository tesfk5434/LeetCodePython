class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix) +1) ]
        for i in range(1, len(matrix)+1):
            for j in range(len(matrix[0])):
                dp[i][j] = dp[i-1][j] + 1 if matrix[i-1][j]==1 else 0
        ans += sum(matrix[0])
        for row in range(2,len(matrix)+1):
            for col in range(len(matrix[0])):
                height = dp[row][col]
                minimumHeight = height
                if height>0:
                    ans += 1
                for dist in range(1, min(height, len(matrix[0])-col)):
                    minimumHeight = min(minimumHeight, dp[row][col+dist])
                    if minimumHeight<dist+1:
                        break    
                    ans += 1
        return ans
                


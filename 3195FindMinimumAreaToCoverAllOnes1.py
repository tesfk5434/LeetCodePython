class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        x1,x2,y1,y2 = float('inf'), float('-inf'), float('inf'), float('-inf')
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    y1 = min(y1, row)
                    y2 = max(y2, row)
                    x1 = min(x1, col)
                    x2 = max(x2, col)
        return (x2-x1 + 1)*(y2-y1 + 1)
        
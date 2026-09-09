class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum=0
        rows=len(grid)
        cols=len(grid[0])
        for i in range(rows-2):
            for j in range(cols-2):
                sum_=(grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2])

                if sum_>max_sum:
                    max_sum=sum_
        return max_sum

        
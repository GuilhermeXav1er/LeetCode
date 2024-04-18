class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    p += 4
                    if j > 0 and grid[i][j-1] == 1:
                        p -= 2
                    if i > 0 and grid[i-1][j] == 1:
                        p -= 2
        return p
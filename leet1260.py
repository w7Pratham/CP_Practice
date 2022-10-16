class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for _ in range(k):
            grid[0].insert(0, grid[len(grid) - 1].pop())
            for j in range(1,len(grid)):
                grid[j].insert(0,grid[j-1].pop())
        return grid

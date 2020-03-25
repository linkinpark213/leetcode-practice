from typing import List


class Solution:
    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        grid[i][j] = '0'
        if i > 0 and grid[i - 1][j] == '1':
            self.dfs(grid, i - 1, j)
        if i < len(grid) - 1 and grid[i + 1][j] == '1':
            self.dfs(grid, i + 1, j)
        if j > 0 and grid[i][j - 1] == '1':
            self.dfs(grid, i, j - 1)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
            self.dfs(grid, i, j + 1)
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands([['1', '1', '1', '1', '0'],
                               ['1', '1', '0', '1', '0'],
                               ['1', '1', '0', '0', '0'],
                               ['0', '0', '0', '0', '0']]))
    print(solution.numIslands([['1', '1', '0', '0', '0'],
                               ['1', '1', '0', '0', '0'],
                               ['0', '0', '1', '0', '0'],
                               ['0', '0', '0', '1', '1']]))

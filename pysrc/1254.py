from typing import List


class Solution:
    def clearMainlands(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                self.bfs(grid, i, 0)
            if grid[i][n - 1] == 0:
                self.bfs(grid, i, n - 1)
        for i in range(n):
            if grid[0][i] == 0:
                self.bfs(grid, 0, i)
            if grid[m - 1][i] == 0:
                self.bfs(grid, m - 1, i)
        return grid

    def bfs(self, grid: List[List[int]], i: int, j: int):
        queue = [(i, j)]
        m, n = len(grid), len(grid[0])
        while len(queue) > 0:
            i, j = queue.pop(0)
            grid[i][j] = 1
            for k, l in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if k > 0 and k < m and l > 0 and l < n and grid[k][l] == 0:
                    grid[k][l] = 1
                    queue.append((k, l))
        return

    def closedIsland(self, grid: List[List[int]]) -> int:
        grid = self.clearMainlands(grid)
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                    self.bfs(grid, i, j)
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1, 0],
                                      [1, 0, 0, 0, 0, 1, 1, 0],
                                      [1, 0, 1, 0, 1, 1, 1, 0],
                                      [1, 0, 0, 0, 0, 1, 0, 1],
                                      [1, 1, 1, 1, 1, 1, 1, 0]]))
    print(solution.closedIsland(grid=[[0, 0, 1, 0, 0],
                                      [0, 1, 0, 1, 0],
                                      [0, 1, 1, 1, 0]]))
    print(solution.closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1],
                                      [1, 0, 0, 0, 0, 0, 1],
                                      [1, 0, 1, 1, 1, 0, 1],
                                      [1, 0, 1, 0, 1, 0, 1],
                                      [1, 0, 1, 1, 1, 0, 1],
                                      [1, 0, 0, 0, 0, 0, 1],
                                      [1, 1, 1, 1, 1, 1, 1]]))

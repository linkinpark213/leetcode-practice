from typing import List


class Solution:
    def backtrack(self, grid: List[List[int]], path: List[List[int]], pathLength: int) -> int:
        currI, currJ = path[-1]
        count = 0
        for i, j in [(currI - 1, currJ), (currI + 1, currJ), (currI, currJ - 1), (currI, currJ + 1)]:
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    path.append([i, j])
                    count += self.backtrack(grid, path, pathLength)
                    grid[i][j] = 0
                    path.pop()
                elif grid[i][j] == 2 and len(path) == pathLength - 1:
                    count += 1
        return count

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        startI, startJ = 0, 0
        obstacles = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    startI, startJ = i, j
                elif grid[i][j] == -1:
                    obstacles += 1
        path = [[startI, startJ]]
        return self.backtrack(grid, path, len(grid) * len(grid[0]) - obstacles)


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsIII([[1, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 2, -1]]))
    print(solution.uniquePathsIII([[1, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 2]]))
    print(solution.uniquePathsIII([[0, 1],
                                   [2, 0]]))

from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] > 0:
                    count += 2
                    count += max(0, grid[i][j] - grid[i - 1][j]) if i > 0 else grid[i][j]
                    count += max(0, grid[i][j] - grid[i][j - 1]) if j > 0 else grid[i][j]
                    count += max(0, grid[i][j] - grid[i + 1][j]) if i < len(grid) - 1 else grid[i][j]
                    count += max(0, grid[i][j] - grid[i][j + 1]) if j < len(grid) - 1 else grid[i][j]
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.surfaceArea([[2]]) == 10)
    print(solution.surfaceArea([[1, 2],
                                [3, 4]]) == 34)
    print(solution.surfaceArea([[1, 0],
                                [0, 2]]) == 16)
    print(solution.surfaceArea([[1, 1, 1],
                                [1, 0, 1],
                                [1, 1, 1]]) == 32)
    print(solution.surfaceArea([[2, 2, 2],
                                [2, 1, 2],
                                [2, 2, 2]]) == 46)

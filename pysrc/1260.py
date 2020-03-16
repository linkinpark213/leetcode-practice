from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        newGrid = [[0] * n for _ in range(m)]
        for i in range(m * n):
            newGrid[((i + k) // n) % m][(i + k) % n] = grid[i // n][i % n]
        return newGrid


if __name__ == '__main__':
    solution = Solution()
    print(solution.shiftGrid([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]], 1))

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotQueue = []
        orangeCount = 0
        orangeRotted = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    orangeCount += 1
                if grid[row][col] == 2:
                    rotQueue.append(((row, col), 0))

        day = 0
        while len(rotQueue) != 0:
            orangeRotted += 1
            (row, col), day = rotQueue.pop(0)
            for i, j in [[row, col + 1], [row, col - 1], [row + 1, col], [row - 1, col]]:
                if (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1):
                    grid[i][j] = 2
                    rotQueue.append(((i, j), day + 1))

        return day if orangeRotted == orangeCount else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))

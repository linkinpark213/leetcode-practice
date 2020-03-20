from typing import List


class Solution:
    def isSquare(self, grid: List[List[int]], i: int, j: int, size: int) -> bool:
        for k in range(1, size):
            if grid[i + k][j] != 1 or grid[i + k][j + size - 1] != 1 or grid[i][j + k] != 1 or grid[i + size - 1][
                j + k] != 1:
                return False
        return True

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        maxSize = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    size = 1
                    while i + size < height and j + size < width and grid[i + size][j] == 1 and grid[i][
                        j + size] == 1:
                        size += 1
                    while size > maxSize:
                        if self.isSquare(grid, i, j, size):
                            maxSize = max(maxSize, size)
                        size -= 1

        return maxSize ** 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.largest1BorderedSquare(grid=[[1, 1, 1],
                                                [1, 0, 1],
                                                [1, 1, 1]]))
    print(solution.largest1BorderedSquare(grid=[[1, 1, 0, 0]]))

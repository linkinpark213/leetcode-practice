from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        numKills = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    for r in [range(1, len(grid) - i), range(-1, -i - 1, -1)]:
                        for di in r:
                            if grid[i + di][j] == '0':
                                numKills[i + di][j] += 1
                            elif grid[i + di][j] == 'W':
                                break
                    for r in [range(1, len(grid[0]) - j), range(-1, -j - 1, -1)]:
                        for dj in r:
                            if grid[i][j + dj] == '0':
                                numKills[i][j + dj] += 1
                            elif grid[i][j + dj] == 'W':
                                break

        return max([max(numKills[i]) for i in range(len(numKills))])


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxKilledEnemies([["0", "E", "0", "0"],
                                     ["E", "0", "W", "E"],
                                     ["0", "E", "0", "0"]]))

import sys
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dp = [[sys.maxsize] * N for _ in range(N)]
        dp[0][0] = grid[0][0]
        queue = [(0, 0)]
        while len(queue) > 0:
            i, j = queue.pop(0)
            for k, l in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if k >= 0 and k < N and l >= 0 and l < N:
                    if dp[i][j] > dp[k][l]:
                        dp[i][j] = max(dp[k][l], grid[i][j])
                    elif dp[i][j] < dp[k][l]:
                        dp[k][l] = max(dp[i][j], grid[i][j], grid[k][l])
                        queue.append((k, l))
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.swimInWater([[0, 2], [1, 3]]))
    print(solution.swimInWater([[0, 1, 2, 3, 4],
                                [24, 23, 22, 21, 5],
                                [12, 13, 14, 15, 16],
                                [11, 17, 18, 19, 20],
                                [10, 9, 8, 7, 6]]))
    print(solution.swimInWater([[26, 99, 80, 1, 89, 86, 54, 90, 47, 87],
                                [9, 59, 61, 49, 14, 55, 77, 3, 83, 79],
                                [42, 22, 15, 5, 95, 38, 74, 12, 92, 71],
                                [58, 40, 64, 62, 24, 85, 30, 6, 96, 52],
                                [10, 70, 57, 19, 44, 27, 98, 16, 25, 65],
                                [13, 0, 76, 32, 29, 45, 28, 69, 53, 41],
                                [18, 8, 21, 67, 46, 36, 56, 50, 51, 72],
                                [39, 78, 48, 63, 68, 91, 34, 4, 11, 31],
                                [97, 23, 60, 17, 66, 37, 43, 33, 84, 35],
                                [75, 88, 82, 20, 7, 73, 2, 94, 93, 81]]))

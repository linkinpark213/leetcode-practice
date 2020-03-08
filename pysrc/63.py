from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = []
        for i in range(m):
            memo.append([0] * n)

        memo[m - 1][n - 1] = 1 if obstacleGrid[m - 1][n - 1] != 1 else 0

        queue = [(m - 1, n - 1)]
        while len(queue) != 0:
            i, j = queue.pop(0)
            if i + 1 < m:
                memo[i][j] += memo[i + 1][j]
            if j + 1 < n:
                memo[i][j] += memo[i][j + 1]
            if i > 0 and obstacleGrid[i - 1][j] != 1:
                if (i - 1, j) not in queue:
                    queue.append((i - 1, j))
            if j > 0 and obstacleGrid[i][j - 1] != 1:
                if (i, j - 1) not in queue:
                    queue.append((i, j - 1))
        return memo[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsWithObstacles([[0, 0, 0],
                                             [0, 1, 0],
                                             [0, 0, 0]]))
    print(solution.uniquePathsWithObstacles([[1]]))

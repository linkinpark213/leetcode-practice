from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[0] * len(dungeon[0]) for _ in range(len(dungeon))]
        dp[-1][-1] = max(1, -dungeon[-1][-1] + 1)

        for i in range(len(dungeon) - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])

        for i in range(len(dungeon[0]) - 2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i + 1] - dungeon[-1][i])

        for i in range(len(dungeon) - 2, -1, -1):
            for j in range(len(dungeon[0]) - 2, -1, -1):
                dp[i][j] = min(max(1, dp[i + 1][j] - dungeon[i][j]), max(1, dp[i][j + 1] - dungeon[i][j]))

        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculateMinimumHP(dungeon=[[-2, -3, 3],
                                               [-5, -10, 1],
                                               [10, 30, -5]]))
    print(solution.calculateMinimumHP(dungeon=[[100]]))

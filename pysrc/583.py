from typing import List


class MemoSolution:
    def lcs(self, word1: str, word2: str, i: int, j: int, memo: List[List[int]]) -> int:
        if i == len(word1) or j == len(word2):
            return 0
        elif memo[i][j] != -1:
            return memo[i][j]
        else:
            if word1[i] == word2[j]:
                length = 1 + self.lcs(word1, word2, i + 1, j + 1, memo)
            else:
                length = max(self.lcs(word1, word2, i, j + 1, memo), self.lcs(word1, word2, i + 1, j, memo))
            memo[i][j] = length
            return length

    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[-1] * len(word2) for _ in range(len(word1))]
        return len(word1) + len(word2) - 2 * self.lcs(word1, word2, 0, 0, memo)


class DPSolution:
    def lcs(self, word1: str, word2: str) -> int:
        dp = [[0] * 2 for _ in range(2)]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        return len(word1) + len(word2) - 2 * self.lcs(word1, word2)


if __name__ == '__main__':
    for solution in [MemoSolution(), DPSolution()]:
        print(solution.minDistance("sea", "eat"))

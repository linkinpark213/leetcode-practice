from typing import List


class Solution:
    def longestPathFrom(self, matrix, i, j, memo):
        if memo[i][j] > 0:
            return memo[i][j]

        m, n = len(matrix), len(matrix[0])
        longestPath = 1

        for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if k >= 0 and k < m and l >= 0 and l < n and matrix[k][l] < matrix[i][j]:
                fullPath = self.longestPathFrom(matrix, k, l, memo)
                if fullPath + 1 > longestPath:
                    longestPath = 1 + fullPath
        memo[i][j] = longestPath
        return longestPath

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        longestPath = 1
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                lenPath = self.longestPathFrom(matrix, i, j, memo)
                if lenPath > longestPath:
                    longestPath = lenPath
        return longestPath


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestIncreasingPath(matrix=[[9, 9, 4],
                                                 [6, 6, 8],
                                                 [2, 1, 1]]) == 4)
    print(solution.longestIncreasingPath(matrix=[[7, 8, 9],
                                                 [9, 7, 6],
                                                 [7, 2, 3]]) == 6)
    print(solution.longestIncreasingPath(matrix=[[3, 4, 5],
                                                 [3, 2, 6],
                                                 [2, 2, 1]]) == 4)

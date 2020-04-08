from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp


if __name__ == '__main__':
    solution = Solution()
    print(solution.rotate([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]))
    print(solution.rotate([[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12],
                           [13, 14, 15, 16]]))

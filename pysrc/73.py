from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for i in rows:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0

        return


if __name__ == '__main__':
    solution = Solution()
    print(solution.setZeroes([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]))
    print(solution.setZeroes([
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]))

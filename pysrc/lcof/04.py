from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    break
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.findNumberIn2DArray([[1, 4, 7, 11, 15],
                                        [2, 5, 8, 12, 19],
                                        [3, 6, 9, 16, 22],
                                        [10, 13, 14, 17, 24],
                                        [18, 21, 23, 26, 30]], target=5))
    print(solution.findNumberIn2DArray([[1, 4, 7, 11, 15],
                                        [2, 5, 8, 12, 19],
                                        [3, 6, 9, 16, 22],
                                        [10, 13, 14, 17, 24],
                                        [18, 21, 23, 26, 30]], target=20))

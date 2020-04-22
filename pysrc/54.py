from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        ans = []
        level = 0
        m, n = len(matrix), len(matrix[0])
        while level <= min((m - 1) // 2, (n - 1) // 2):
            for i in range(level, n - level):
                ans.append(matrix[level][i])
            for i in range(level + 1, m - level - 1):
                ans.append(matrix[i][n - level - 1])
            if level != m - level - 1:
                for i in range(n - level - 1, level - 1, -1):
                    ans.append(matrix[m - level - 1][i])
            if level != n - level - 1:
                for i in range(m - level - 2, level, -1):
                    ans.append(matrix[i][level])
            level += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
    print(solution.spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]))
    print(solution.spiralOrder([[3], [2]]))

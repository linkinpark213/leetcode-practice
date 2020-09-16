from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        sums = [[0] * n for _ in range(m)]
        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            sums[i][0] = mat[i][0]
            for j in range(1, n):
                sums[i][j] = sums[i][j - 1] + mat[i][j]
        for j in range(n):
            for i in range(1, m):
                sums[i][j] += sums[i - 1][j]

        for i in range(m):
            for j in range(n):
                t, l, b, r = max(0, i - K), max(0, j - K), min(m - 1, i + K), min(n - 1, j + K)
                answer[i][j] = sums[b][r]
                if t > 0:
                    answer[i][j] -= sums[t - 1][r]
                if l > 0:
                    answer[i][j] -= sums[b][l - 1]
                if l > 0 and t > 0:
                    answer[i][j] += sums[t - 1][l - 1]

        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=1))
    print(solution.matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=2))

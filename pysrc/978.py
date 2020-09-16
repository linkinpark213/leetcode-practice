from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        dp = [[1] * n for _ in range(2)]
        for i in range(1, n):
            if A[i] < A[i - 1]:
                dp[0][i] = dp[1][i - 1] + 1
            if A[i] > A[i - 1]:
                dp[1][i] = dp[0][i - 1] + 1
        return max(max(dp[0]), max(dp[1]))


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
    print(solution.maxTurbulenceSize([4, 8, 12, 16]))
    print(solution.maxTurbulenceSize([100]))

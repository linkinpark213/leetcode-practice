from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeros = [0] * len(strs)
        ones = [0] * len(strs)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i, s in enumerate(strs):
            for c in s:
                if c == '0':
                    zeros[i] += 1
                else:
                    ones[i] += 1

        for i in range(1, len(strs) + 1):
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j >= zeros[i - 1] and k >= ones[i - 1]:
                        dp[j][k] = max(dp[j][k], 1 + dp[j - zeros[i - 1]][k - ones[i - 1]])

        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
    print(solution.findMaxForm(strs=["10", "0", "1"], m=1, n=1))

from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if max(arr) < 0:
            return max(arr)

        maxSum = min(arr)
        dp = [maxSum] * 2
        for i, num in enumerate(arr):
            temp = max(dp[0], 0) + num
            dp[1] = max(dp[0], dp[1] + num)
            dp[0] = temp
            maxSum = max(maxSum, dp[0], dp[1])

        return maxSum


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumSum(arr=[1, -2, 0, 3]) == 4)
    print(solution.maximumSum(arr=[1, -2, -2, 3]) == 3)
    print(solution.maximumSum(arr=[-1, -1, -1, -1]) == -1)
    print(solution.maximumSum(arr=[-7, 6, 1, 2, 1, 4, -1]) == 14)
    print(solution.maximumSum(arr=[0, -5, -6, 5, 0, -5]) == 5)
    print(solution.maximumSum(arr=[8, -1, 6, -7, -4, 5, -4, 7, -6]) == 17)
    print(solution.maximumSum(arr=[11, -10, -11, 8, 7, -6, 9, 4, 11, 6, 5, 0]) == 50)

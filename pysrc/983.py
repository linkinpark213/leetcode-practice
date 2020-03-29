from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.insert(0, 0)
        dp = {0: 0}
        for i in range(1, len(days)):
            dp[days[i]] = dp[days[i - 1]] + costs[0]
            j = i
            while j > 0 and days[j] > days[i] - 7:
                j -= 1
            dp[days[i]] = min(dp[days[i]], dp[days[j]] + costs[1])
            while j > 0 and days[j] > days[i] - 30:
                j -= 1
            dp[days[i]] = min(dp[days[i]], dp[days[j]] + costs[2])

        return dp[days[-1]]


if __name__ == '__main__':
    solution = Solution()
    print(solution.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
    print(solution.mincostTickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]))

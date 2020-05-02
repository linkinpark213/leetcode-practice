class Solution:
    def getMoneyAmount(self, n: int) -> int:
        l, r = 1, n
        ans = 0
        while l < r:
            mid = l + (r - l) // 2
            ans += mid
            l = mid + 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.getMoneyAmount(10))
    print(solution.getMoneyAmount(4))

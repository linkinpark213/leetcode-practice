class Solution:
    def waysToChange(self, n: int) -> int:
        count = 0
        while n >= 0:
            count += (1 + n // 10) * (1 + n // 5) - (1 + n // 10) * (n // 10)
            n -= 25
        return count % 1000000007


if __name__ == '__main__':
    solution = Solution()
    print(solution.waysToChange(5))
    print(solution.waysToChange(10))

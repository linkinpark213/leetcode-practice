class Solution:
    def lastRemainingLeft(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return 2 * self.lastRemainingRight(n // 2)

    def lastRemainingRight(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        if n % 2 == 0:
            return 2 * self.lastRemainingLeft(n // 2) - 1
        elif n % 2 == 1:
            return 2 * self.lastRemainingLeft(n // 2)

    def lastRemaining(self, n: int) -> int:
        if n < 2:
            return n
        return self.lastRemainingLeft(n)


if __name__ == '__main__':
    solution = Solution()
    print(solution.lastRemainingLeft(9))

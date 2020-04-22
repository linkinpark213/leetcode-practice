class Solution:
    def myPowHelper(self, x: float, n: int, memo) -> float:
        if n in memo:
            return memo[n]
        r = n % 2
        n = n // 2
        v = self.myPowHelper(x, n, memo)
        v = v * v
        v = v * self.myPowHelper(x, r, memo)
        memo[n * 2 + r] = v
        return v

    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0.0
        if n == 0:
            return 1.0
        if n < 0:
            x = 1.0 / x
        return self.myPowHelper(x, abs(n), {0: 1.0, 1: x})


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2.0, 10))
    print(solution.myPow(2.1, 3))
    print(solution.myPow(2.0, -2))

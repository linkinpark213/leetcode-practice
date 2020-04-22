class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1. / x, -n)
        elif n == 0:
            return 1.
        else:
            v = self.myPow(x, n // 2)
            v *= v
            v *= 1 if n % 2 == 0 else x
            return v


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2.00000, 10))
    print(solution.myPow(2.10000, 3))
    print(solution.myPow(2.00000, -2))

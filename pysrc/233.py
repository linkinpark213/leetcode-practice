class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n < 10:
            return 1
        pow = 1
        while pow * 10 <= n:
            pow *= 10

        count = self.countDigitOne(pow - 1) * (n // pow) + self.countDigitOne(n % pow)
        if n // pow == 1:
            count += n % pow + 1
        else:
            count += pow
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.countDigitOne(n=10))
    print(solution.countDigitOne(n=12))
    print(solution.countDigitOne(n=13))
    print(solution.countDigitOne(n=20))
    print(solution.countDigitOne(n=824883294))

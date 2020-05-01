class Solution:
    def findNthDigit(self, n: int) -> int:
        if n == 0:
            return 0
        count = 1
        pow = 1
        while count + 9 * pow * 10 ** (pow - 1) <= n:
            count += 9 * pow * 10 ** (pow - 1)
            pow += 1
        base, digit = 10 ** (pow - 1) + (n - count) // pow, (n - count) % pow
        print('n = {}, count = {}, pow = {}, base = {}, digit = {}'.format(n, count, pow, base, digit))
        for i in range(pow - digit - 1):
            base = base // 10
        return base % 10


if __name__ == '__main__':
    solution = Solution()
    print(solution.findNthDigit(3))
    print(solution.findNthDigit(10))
    print(solution.findNthDigit(11))
    print(solution.findNthDigit(16))

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        elif n == 4:
            return 4
        elif n % 3 == 0:
            return (3 ** (n // 3)) % 1000000007
        elif n % 3 == 1:
            return (4 * 3 ** ((n - 4) // 3)) % 1000000007
        else:
            return (2 * 3 ** ((n - 2) // 3)) % 1000000007


if __name__ == '__main__':
    solution = Solution()
    print(solution.cuttingRope(2))
    print(solution.cuttingRope(10))

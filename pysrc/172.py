class Solution:
    def count(self, n: int, m: int) -> int:
        count = 0
        while n > 0:
            n = n // m
            count += n
        return count

    def trailingZeroes(self, n: int) -> int:
        return self.count(n, 5)


if __name__ == '__main__':
    solution = Solution()
    print(solution.trailingZeroes(3))
    print(solution.trailingZeroes(5))

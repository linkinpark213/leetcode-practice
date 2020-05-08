class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n = n >> 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(11))
    print(solution.hammingWeight(128))
    print(solution.hammingWeight(2 ** 31 - 3))

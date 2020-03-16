class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 0 and n % 3 == 0:
            n = n // 3
        if n == 1:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfThree(27))
    print(solution.isPowerOfThree(0))
    print(solution.isPowerOfThree(9))
    print(solution.isPowerOfThree(45))

class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        while num > 1 and num % 2 == 0:
            num = num // 2
        while num > 1 and num % 3 == 0:
            num = num // 3
        while num > 1 and num % 5 == 0:
            num = num // 5
        return num == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isUgly(6))
    print(solution.isUgly(8))
    print(solution.isUgly(14))

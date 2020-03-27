class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i = i * 2
        return i - 1 - num


if __name__ == '__main__':
    solution = Solution()
    print(solution.findComplement(5))
    print(solution.findComplement(1))

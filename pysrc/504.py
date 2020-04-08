class Solution:
    def convertToBase7(self, num: int) -> str:
        prefix = ''
        if num < 0:
            prefix = '-'
            num = -num
        s = ''
        while num > 0:
            r = num % 7
            num = num // 7
            s = str(r) + s
        if len(s) == 0:
            s = '0'
        return prefix + s


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToBase7(100))
    print(solution.convertToBase7(-7))

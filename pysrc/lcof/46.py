class Solution:
    def translateStr(self, num: str) -> int:
        if len(num) == 0:
            return 1
        elif len(num) == 1 or num[0] == '0' or ord(num[0]) > ord('2'):
            return self.translateStr(num[1:])
        elif num[0] == '1' or ord(num[1]) < ord('6'):
            return self.translateStr(num[1:]) + self.translateStr(num[2:])
        else:
            return self.translateStr(num[1:])

    def translateNum(self, num: int) -> int:
        return self.translateStr(str(num))


if __name__ == '__main__':
    solution = Solution()
    # print(solution.translateNum(12258))
    print(solution.translateNum(18580))

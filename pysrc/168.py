class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        n = n - 1
        while n >= 0:
            ans = chr(n % 26 + 65) + ans
            n = n // 26 - 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToTitle(1))
    print(solution.convertToTitle(28))
    print(solution.convertToTitle(701))

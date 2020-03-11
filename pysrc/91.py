class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        memo = [[0, 0]]
        if s[0] != '0':
            memo[0][0] = 1
        for i in range(1, len(s)):
            countSeparated = 0
            countCombined = 0
            if s[i - 1] == '1' or (s[i - 1] == '2' and int(s[i]) < 7):
                countCombined = memo[i - 1][0]
            if s[i] != '0':
                countSeparated = memo[i - 1][0] + memo[i - 1][1]
            memo.append([countSeparated, countCombined])

        return memo[-1][0] + memo[-1][1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings('12'))
    print(solution.numDecodings('226'))
    print(solution.numDecodings('0'))
    print(solution.numDecodings('203'))

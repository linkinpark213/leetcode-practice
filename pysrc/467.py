class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        maxDistances = [0] * 26
        length = 1
        for i, c in enumerate(p):
            if maxDistances[ord(c) - ord('a')] == 0:
                maxDistances[ord(c) - ord('a')] = 1
            if i > 0 and (ord(c) - ord(p[i - 1])) % 26 == 1:
                length += 1
                maxDistances[ord(c) - ord('a')] = max(length,
                                                      maxDistances[ord(c) - ord('a')])
            else:
                length = 1

        return sum(maxDistances)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubstringInWraproundString(p='a'))
    print(solution.findSubstringInWraproundString(p='cac'))
    print(solution.findSubstringInWraproundString(p='zab'))
    print(solution.findSubstringInWraproundString(p='abczabc'))

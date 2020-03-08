class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next = [0] * len(needle)
        back = 0
        for i in range(1, len(needle)):
            if needle[i] == needle[back]:
                next[i] = back + 1
                back += 1
            else:
                while back > 0 and needle[i] != needle[back]:
                    back = next[back - 1]
                if needle[i] == needle[back]:
                    next[i] = back + 1
                    back += 1

        back = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[back]:
                back += 1
                if back == len(needle):
                    return i - len(needle) + 1
            else:
                while back > 0 and haystack[i] != needle[back]:
                    back = next[back - 1]
                if haystack[i] == needle[back]:
                    back += 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr('hello', 'll'))
    print(solution.strStr('aaaaa', 'bba'))
    print(solution.strStr('mississippi', 'issip'))
    print(solution.strStr('mississippi', 'issipi'))
    print(solution.strStr('aabaaabaaac', 'aabaaac'))

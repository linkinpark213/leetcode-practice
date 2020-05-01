class Solution:
    def reverseWords(self, s: str) -> str:
        builder = ''
        words = []
        for c in s + ' ':
            if c != ' ':
                builder += c
            elif c == ' ':
                if len(builder) > 0:
                    words.append(builder)
                builder = ''

        ans = ''
        for word in reversed(words):
            ans += word + ' '
        return ans[:-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))
    print(solution.reverseWords("  hello world!  "))
    print(solution.reverseWords("a good   example"))

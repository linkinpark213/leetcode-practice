class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')

        ans = ''
        while len(words) > 0:
            word = words.pop()
            if len(word) > 0:
                ans += word + ' '

        return ans[:-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))
    print(solution.reverseWords("   hello world!"))
    print(solution.reverseWords("a good   example"))

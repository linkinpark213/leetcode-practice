class Solution:
    def compressString(self, S: str) -> str:
        prev = ''
        count = 0
        ans = ''
        for c in S + ' ':
            if c == prev:
                count += 1
            else:
                if count > 0:
                    ans += prev + str(count)
                prev = c
                count = 1

        return ans if len(ans) < len(S) else S


if __name__ == '__main__':
    solution = Solution()
    print(solution.compressString('aabcccccaaa'))
    print(solution.compressString('abbccd'))

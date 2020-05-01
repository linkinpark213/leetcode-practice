class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseLeftWords(s="abcdefg", n=2))
    print(solution.reverseLeftWords(s="lrloseumgh", n=6))

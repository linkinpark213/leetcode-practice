from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for ptr in range(1, len(s) + 1):
            for word in wordDict:
                if len(word) <= ptr and word == s[ptr - len(word):ptr] and dp[ptr - len(word)]:
                    dp[ptr] = True
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(solution.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print(solution.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))

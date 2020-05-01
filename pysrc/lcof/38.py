from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        if len(s) == 1:
            return [s]
        ans = set()
        for i in range(len(s)):
            subs = self.permutation(s[:i] + s[i + 1:])
            for sub in subs:
                ans.add(sub + s[i])
        return list(ans)


if __name__ == '__main__':
    solution = Solution()
    print(solution.permutation('abc'))

from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        depth = -1
        for i, c in enumerate(seq):
            if c == '(':
                depth += 1
                ans.append(depth % 2)
            else:
                ans.append(depth % 2)
                depth -= 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDepthAfterSplit(seq="(()())"))
    print(solution.maxDepthAfterSplit(seq="()(())()"))
    print(solution.maxDepthAfterSplit(seq="(((()))((())))"))

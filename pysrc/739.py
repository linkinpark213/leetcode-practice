from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        for i, t in enumerate(T):
            while len(stack) > 0 and stack[-1][1] < t:
                j, k = stack.pop()
                ans[j] = i - j
            stack.append((i, t))
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(solution.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))

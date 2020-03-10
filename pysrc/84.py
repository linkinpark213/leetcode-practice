from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        heights = [0] + heights + [0]
        maxArea = 0
        stack = []
        for i, height in enumerate(heights):
            while len(stack) > 0 and heights[stack[-1]] > height:
                prevHeight = stack.pop(-1)
                maxArea = max(maxArea, heights[prevHeight] * (i - stack[-1] - 1))
            stack.append(i)
        return maxArea


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(solution.largestRectangleArea([1, 1]))
    print(solution.largestRectangleArea(list(range(20000))))

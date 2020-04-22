from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxA = 0
        while l < r:
            maxA = max(maxA, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxA


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))

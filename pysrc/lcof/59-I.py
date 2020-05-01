from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = []
        for i, num in enumerate(nums):
            if len(queue) > 0 and queue[0][0] <= i - k:
                queue.pop(0)
            while len(queue) > 0 and queue[-1][1] < num:
                queue.pop()
            queue.append((i, num))
            ans.append(queue[0][1])
        return ans[k - 1:]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

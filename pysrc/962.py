from typing import List


class Solution:
    def search(self, A: List[int], arr: List[int], num: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if A[arr[mid]] > num:
                l = mid + 1
            elif A[arr[mid]] == num:
                return mid
            elif A[arr[mid]] < num:
                r = mid - 1
        return l

    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        maxWidth = 0
        for i, num in enumerate(A):
            if len(stack) == 0 or A[stack[-1]] > num:
                stack.append(i)
            else:
                maxWidth = max(maxWidth, i - stack[self.search(A, stack, num)])
        return maxWidth


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxWidthRamp([6, 0, 8, 2, 1, 5]) == 4)
    print(solution.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7)
    print(solution.maxWidthRamp([4, 2, 1, 3]) == 2)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[mid] >= nums[left] or nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > target:
                if nums[mid] < nums[left] or nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(solution.search([5, 1, 3], 3))

from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int, l: int, r: int) -> int:
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return 1 + self.binarySearch(nums, target, l, mid) + self.binarySearch(nums, target, mid + 1, r)
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return 0

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums))


if __name__ == '__main__':
    solution = Solution()
    print(solution.search(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(solution.search(nums=[5, 7, 7, 8, 8, 10], target=6))

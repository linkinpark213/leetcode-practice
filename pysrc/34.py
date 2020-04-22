from typing import List


class Solution:
    def searchLeft(self, nums: List[int], target: int, l: int, r: int) -> int:
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

    def searchRight(self, nums: List[int], target: int, l: int, r: int) -> int:
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                if mid == l:
                    return l if nums[r] != target else r
                l = mid
        return r

    def searchRangeHelper(self, nums: List[int], target: int, l: int, r: int) -> List[int]:
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return [self.searchLeft(nums, target, l, mid), self.searchRight(nums, target, mid, r)]
        return [-1, -1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.searchRangeHelper(nums, target, 0, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
    print(solution.searchRange(nums=[1], target=1))

from typing import List


class Solution:
    def swap(self, nums: List[int], l: int, r: int):
        nums[l] = nums[l] + nums[r]
        nums[r] = nums[l] - nums[r]
        nums[l] = nums[l] - nums[r]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            while l <= r and nums[l] >= pivot:
                l += 1
            while l <= r and nums[r] < pivot:
                r -= 1
            if l < r:
                self.swap(nums, l, r)
        if r > k - 1:
            print('Looking for {}th in {}'.format(k, nums[:l]))
            return self.findKthLargest(nums[:l], k)
        elif r < k - 1:
            print('Looking for {}th in {}'.format(k - l, nums[l:]))
            return self.findKthLargest(nums[l:], k - l)
        else:
            print('Found at #{} of {}'.format(r, nums))
            return nums[r]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
    print(solution.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
    print(solution.findKthLargest(nums=[3, 1, 2, 4], k=2))

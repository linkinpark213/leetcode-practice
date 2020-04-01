from typing import List


class Solution:
    def swap(self, nums: List[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def fastSort(self, nums: List[int], l: int, r: int) -> List[int]:
        if l >= r:
            return nums

        pivot = nums[l]
        lptr, rptr = l, r
        while lptr < rptr:
            while lptr < rptr and nums[rptr] >= pivot:
                rptr -= 1
            while lptr < rptr and nums[lptr] < pivot:
                lptr += 1
            self.swap(nums, lptr, rptr)
        self.fastSort(nums, l, lptr)
        self.fastSort(nums, rptr + 1, r)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.fastSort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortArray(nums=[5, 2, 3, 1]))
    print(solution.sortArray(nums=[5, 1, 1, 2, 0, 0]))

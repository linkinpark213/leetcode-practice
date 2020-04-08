from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, ptr = m - 1, n - 1, m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p2 < 0 or p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[ptr] = nums1[p1]
                p1 -= 1
            else:
                nums1[ptr] = nums2[p2]
                p2 -= 1
            ptr -= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))

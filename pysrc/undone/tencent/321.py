from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = [0] * k
        for i in range(max(k - len(nums2), 0), min(len(nums1), k) + 1):
            sub1 = self.maxKSubsequence(nums1, i)
            sub2 = self.maxKSubsequence(nums2, k - i)
            print('merging {} and {}'.format(sub1, sub2))
            ans = self.max(ans, self.merge(sub1, sub2))
        return ans

    def max(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            if nums1[i] > nums2[i]:
                return nums1
            elif nums2[i] > nums1[i]:
                return nums2
        return nums1

    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        ptr1, ptr2 = 0, 0
        while ptr1 < len(nums1) or ptr2 < len(nums2):
            if ptr1 == len(nums1) or ptr2 < len(nums2) and nums1[ptr1] < nums2[ptr2]:
                ans.append(nums2[ptr2])
                ptr2 += 1
            elif ptr2 == len(nums2) or ptr1 < len(nums1) and nums2[ptr2] < nums1[ptr1]:
                ans.append(nums1[ptr1])
                ptr1 += 1
            elif nums1[ptr1] == nums2[ptr2]:
                temp1, temp2 = ptr1, ptr2
                while temp1 < len(nums1) and temp2 < len(nums2) and nums1[temp1] == nums2[temp2]:
                    temp1 += 1
                    temp2 += 1
                if temp1 == len(nums1) or temp2 != len(nums2) and nums1[temp1] < nums2[temp2]:
                    ans.append(nums2[ptr2])
                    ptr2 += 1
                else:
                    ans.append(nums1[ptr1])
                    ptr1 += 1

        return ans

    def maxKSubsequence(self, nums: List[int], k: int) -> List[int]:
        abandon = len(nums) - k
        if abandon == 0:
            return nums
        elif k == 0:
            return []
        stack = []
        i = 0
        while i < len(nums):
            while abandon > 0 and len(stack) > 0 and nums[i] > stack[-1]:
                stack.pop()
                abandon -= 1
            stack.append(nums[i])
            i += 1
        while abandon > 0:
            stack.pop()
            abandon -= 1
        return stack


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxNumber(nums1=[3, 4, 6, 5], nums2=[9, 1, 2, 5, 8, 3], k=5))
    print(solution.maxNumber(nums1=[6, 7], nums2=[6, 0, 4], k=5))
    print(solution.maxNumber(nums1=[3, 9], nums2=[8, 9], k=3))
    print(solution.maxNumber(nums1=[2, 5, 6, 4, 4, 0], nums2=[7, 3, 8, 0, 6, 5, 7, 6, 2], k=15))

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        m, n = len(nums1), len(nums2)
        iMin, iMax = 0, m
        while iMin <= iMax:
            i = (iMin + iMax) // 2
            j = (m + n + 1) // 2 - i
            if j != 0 and i != m and nums2[j - 1] > nums1[i]:
                iMin = i + 1
            elif i != 0 and j != n and nums1[i - 1] > nums2[j]:
                iMax = i - 1
            else:
                if i == 0:
                    maxLeft = nums2[j - 1]
                elif j == 0:
                    maxLeft = nums1[i - 1]
                else:
                    maxLeft = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return maxLeft

                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums2[j], nums1[i])

                return (maxLeft + minRight) / 2.0

        return 0.0


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
    print(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))


from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        common = set()
        for num in nums1:
            if num not in set1:
                set1.add(num)

        for num in nums2:
            if num in set1:
                common.add(num)
        return sorted(common)


if __name__ == '__main__':
    solution = Solution()
    print(solution.intersection([1, 2, 2, 1], [2, 2]))
    print(solution.intersection([4, 9, 5], [9, 4, 8, 5, 4]))

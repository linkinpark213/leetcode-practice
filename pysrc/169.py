from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq.keys():
                freq[num] = 0
            freq[num] += 1

        for num in freq.keys():
            if freq[num] > len(nums) // 2:
                return num
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))

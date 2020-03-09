from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        first = {}
        last = {}
        maxFreq = 1
        maxNum = nums[0]
        for i, num in enumerate(nums):
            last[num] = i
            if num in freq.keys():
                freq[num] += 1
                if freq[num] > maxFreq or freq[num] == maxFreq and i - first[num] < last[maxNum] - first[maxNum]:
                    maxNum = num
                    maxFreq = freq[num]
            else:
                freq[num] = 1
                first[num] = i

        print('maxNum = {}'.format(maxNum))

        left = 0
        right = len(nums) - 1
        while nums[left] != maxNum:
            left += 1
        while nums[right] != maxNum:
            right -= 1
        return right - left + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findShortestSubArray([1, 2, 2, 3, 1]))
    print(solution.findShortestSubArray([6, 2, 2, 3, 1, 4, 2]))
    print(solution.findShortestSubArray([2, 1, 1, 2, 1, 3, 3, 3, 1, 3, 1, 3, 2]))

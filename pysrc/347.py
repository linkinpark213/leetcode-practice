from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencies = {}
        for num in nums:
            if num not in numFrequencies.keys():
                numFrequencies[num] = 1
            else:
                numFrequencies[num] += 1

        frequencyNums = {}
        for num, frequency in numFrequencies.items():
            if frequency not in frequencyNums.keys():
                frequencyNums[frequency] = [num]
            else:
                frequencyNums[frequency].append(num)

        frequencies = list(frequencyNums.keys())
        frequencies.sort()
        frequencies.reverse()
        count = 0
        ptr = 0
        ans = []
        while count < k:
            frequency = frequencies[ptr]
            nums = frequencyNums[frequency]
            nums.sort()
            ans.extend(nums)
            count += len(frequencyNums[frequency])
            ptr += 1

        while len(ans) > k:
            ans.pop(-1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(solution.topKFrequent([1], 1))

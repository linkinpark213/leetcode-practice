from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        numSum = {0: 1}
        for num in nums:
            sum += num
            if sum - k in numSum.keys():
                count += numSum[sum - k]
            if sum not in numSum.keys():
                numSum[sum] = 0
            numSum[sum] += 1
        print(numSum)
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))
    print(solution.subarraySum([1], 1))
    print(solution.subarraySum([1], 0))

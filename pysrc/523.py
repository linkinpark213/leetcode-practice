from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        k = abs(k)
        for i in range(1, len(nums)):
            if nums[i] == 0 and nums[i - 1] == 0:
                return True
        d = {0: -1}
        if k > 0:
            sum = 0
            for i, num in enumerate(nums):
                sum = (sum + num) % k
                if sum in d.keys():
                    if i - d[sum] > 1:
                        return True
                else:
                    d[sum] = i

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
    print(solution.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6))
    print(solution.checkSubarraySum(nums=[1, 1], k=1))

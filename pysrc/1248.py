from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        steps = [1]
        oddCount = 0
        for i, num in enumerate(nums):
            if num % 2 == 1:
                oddCount += 1
                steps.append(1)
            else:
                steps[-1] += 1

        return sum([steps[n] * steps[n - k] for n in range(k, len(steps))])


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
    print(solution.numberOfSubarrays(nums=[2, 4, 6], k=1))
    print(solution.numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximums = [1]
        minimums = [1]
        for i, num in enumerate(nums):
            maximums.append(max(num, maximums[i] * num, minimums[i] * num))
            minimums.append(min(num, minimums[i] * num, maximums[i] * num))
        print('maxes: ', maximums[1:])
        print('mins: ', minimums[1:])
        return max(maximums[1:])


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([2, 3, -2, 4]))
    print(solution.maxProduct([-2, 0, -1]))
    print(solution.maxProduct([-2, 3, -4]))
    print(solution.maxProduct([-4, -3, -2]))

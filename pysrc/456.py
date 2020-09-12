from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        leftMins = []
        for num in nums:
            leftMins.append(num if len(leftMins) == 0 or leftMins[-1] > num else leftMins[-1])

        print('Left minimums: ', leftMins)

        for i in range(1, len(nums) - 1):
            if leftMins[i] < nums[i]:
                for j in range(i + 1, len(nums)):
                    if nums[j] > leftMins[i] and nums[j] < nums[i]:
                        return True

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.find132pattern([1, 2, 3, 4]) == False)
    print(solution.find132pattern([3, 1, 4, 2]) == True)
    print(solution.find132pattern([-1, 3, 2, 0]) == True)
    print(solution.find132pattern([3, 5, 0, 3, 4]) == True)
    print(solution.find132pattern([1, 0, 1, -4, -3]) == False)
    print(solution.find132pattern([-2, 1, 2, -2, 1, 2]) == True)
    print(solution.find132pattern([2, 4, 3, 1]) == True)

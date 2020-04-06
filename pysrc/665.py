from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        stack = []
        count = 0
        for num in nums:
            if len(stack) == 0 or stack[-1] <= num:
                stack.append(num)
            elif len(stack) == 1 or stack[-2] <= num:
                stack[-1] = num
                count += 1
            else:
                count += 1
        return count <= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPossibility(nums=[4, 2, 3]))
    print(solution.checkPossibility(nums=[4, 2, 1]))
    print(solution.checkPossibility(nums=[3, 4, 2, 3]))

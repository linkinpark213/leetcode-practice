from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i in range(len(nums) - 1):
            ans.append(ans[-1] * nums[i])
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * suffix
            suffix = suffix * nums[i]
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))

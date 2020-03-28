from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) == 0 or k == 0:
            return False
        nums = sorted([(i, num) for i, num in enumerate(nums)], key=lambda x: x[1])
        fast = 1
        slow = 0
        while fast < len(nums):
            while slow < fast - 1 and nums[fast][1] > nums[slow][1] + t:
                slow += 1
            if nums[fast][1] <= nums[slow][1] + t and abs(nums[slow][0] - nums[fast][0]) <= k:
                return True
            fast += 1

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0) == True)
    print(solution.containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2) == True)
    print(solution.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3) == False)
    print(solution.containsNearbyAlmostDuplicate(nums=[2, 2], k=3, t=0) == True)

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) == 0 or k == 0 or t < 0:
            return False
        bucket = dict()
        for i, num in enumerate(nums):
            bucketNum = num // (t + 1)
            if bucketNum in bucket:
                return True
            elif bucketNum + 1 in bucket and abs(bucket[bucketNum + 1] - num) <= t:
                return True
            elif bucketNum - 1 in bucket and abs(bucket[bucketNum - 1] - num) <= t:
                return True
            bucket[bucketNum] = num
            if i >= k:
                bucket.pop(nums[i - k] // (t + 1))

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0) == True)
    print(solution.containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2) == True)
    print(solution.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3) == False)
    print(solution.containsNearbyAlmostDuplicate(nums=[2, 2], k=3, t=0) == True)

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = list(range(n))
        ptr = 0
        while len(nums) > 1:
            ptr = (ptr - 1 + m) % len(nums)
            nums.pop(ptr)
        return nums[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.lastRemaining(n=5, m=3))
    print(solution.lastRemaining(n=10, m=17))

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 6:
            return n
        nums = [0, 1, 2, 3, 4, 5, 6]
        p2, p3, p5 = 1, 1, 1
        for i in range(6, n):
            while nums[p2] * 2 <= nums[-1]:
                p2 += 1
            while nums[p3] * 3 <= nums[-1]:
                p3 += 1
            while nums[p5] * 5 <= nums[-1]:
                p5 += 1
            if nums[p2] * 2 < nums[p3] * 3 and nums[p2] * 2 < nums[p5] * 5:
                nums.append(nums[p2] * 2)
                p2 += 1
            elif nums[p3] * 3 < nums[p5] * 5:
                nums.append(nums[p3] * 3)
                p3 += 1
            else:
                nums.append(nums[p5] * 5)
                p5 += 1
        return nums[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.nthUglyNumber(n=10))

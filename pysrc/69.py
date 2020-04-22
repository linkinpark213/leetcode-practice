class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        else:
            ans = self.mySqrt(x >> 2) << 1
            if (ans + 1) * (ans + 1) > x:
                return ans
            return ans + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(4))
    print(solution.mySqrt(8))

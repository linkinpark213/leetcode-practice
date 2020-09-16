class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        while n > 1:
            i = 2
            while i <= n:
                if n % i == 0:
                    n = n // i
                    ans += i
                    break
                i += 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSteps(1))
    print(solution.minSteps(3))
    print(solution.minSteps(6))
    print(solution.minSteps(18))

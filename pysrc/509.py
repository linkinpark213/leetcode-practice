class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        ans = [0, 1]
        for i in range(1, N):
            ans[1] = ans[0] + ans[1]
            ans[0] = ans[1] - ans[0]
        return ans[1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.fib(2))
    print(solution.fib(3))
    print(solution.fib(4))

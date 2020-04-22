class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prev = [0, 1]
        for i in range(1, n):
            prev[1] = prev[0] + prev[1]
            prev[0] = prev[1] - prev[0]
        return prev[1] % 1000000008


if __name__ == '__main__':
    solution = Solution()
    print(solution.fib(0))
    print(solution.fib(1))
    print(solution.fib(2))
    print(solution.fib(3))
    print(solution.fib(4))
    print(solution.fib(5))
    print(solution.fib(6))

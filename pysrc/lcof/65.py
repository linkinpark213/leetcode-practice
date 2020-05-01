class Solution:
    def add(self, a: int, b: int) -> int:
        min = 0xffffffff
        max = 0x7fffffff
        a, b = a & min, b & min
        while b != 0:
            a, b = a ^ b, ((a & b)) << 1 & min
        return a if a <= max else ~(a ^ min)


if __name__ == '__main__':
    solution = Solution()
    print(solution.add(1, 1))
    print(solution.add(999, 1001))
    print(solution.add(-1, 2))

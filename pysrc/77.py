from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k:
            return []
        elif k == 1:
            return [[i] for i in range(1, n + 1)]
        elif n == k:
            return [list(range(1, n + 1))]
        return self.combine(n - 1, k) + [suffix + [n] for suffix in self.combine(n - 1, k - 1)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(n=4, k=2))
    print(solution.combine(n=3, k=2))
    print(solution.combine(n=2, k=2))
    print(solution.combine(n=3, k=1))

class Solution:
    def sumNums(self, n: int) -> int:
        return n and self.sumNums(n - 1) + n


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumNums(10))

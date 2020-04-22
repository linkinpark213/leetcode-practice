from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10 ** n))


if __name__ == '__main__':
    solution = Solution()
    print(solution.printNumbers(n=1))

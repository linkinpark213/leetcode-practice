from typing import List


class Solution:
    def twoSum(self, n: int) -> List[float]:
        if n == 1:
            return [1. / 6.] * 6
        else:
            suffix = self.twoSum(n - 1)
            ans = [0.] * (n * 6 - n + 1)
            for i in range(n, n * 6 + 1):
                ans[i - n] = sum([suffix[j] * (1. / 6.) for j in range(i - n - 5, i - n + 1) if j >= 0 and j < len(suffix)])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(1))
    print(solution.twoSum(2))

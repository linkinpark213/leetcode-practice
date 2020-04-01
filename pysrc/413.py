from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        subArrays = [0] * len(A)
        diff = [0] * len(A)
        count = 0
        for i in range(1, len(A)):
            diff[i] = A[i] - A[i - 1]
            if i >= 2:
                if diff[i] == diff[i - 1]:
                    count += 1
                else:
                    count = 0
                if count > 0:
                    subArrays[i] = count
        return sum(subArrays)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfArithmeticSlices([1, 2, 3, 4]))
    print(solution.numberOfArithmeticSlices([7, 7, 7, 7]))

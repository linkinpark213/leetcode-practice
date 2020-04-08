from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestPerimeter([2, 1, 2]))
    print(solution.largestPerimeter([1, 2, 1]))
    print(solution.largestPerimeter([3, 2, 3, 4]))
    print(solution.largestPerimeter([3, 6, 2, 3]))

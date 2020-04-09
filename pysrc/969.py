from typing import List


class Solution:
    def findMax(self, A: List[int], r: int) -> int:
        max = A[0]
        pos = 0
        for i in range(1, r):
            if max < A[i]:
                pos = i
                max = A[i]
        return pos

    def pancakeSort(self, A: List[int]) -> List[int]:
        flips = []
        for r in range(len(A), 0, -1):
            maxPos = self.findMax(A, r)
            if maxPos != r - 1:
                if maxPos > 0:
                    A[:maxPos + 1] = A[maxPos::-1]
                    flips.append(maxPos + 1)
                A[:r] = A[r - 1::-1]
                flips.append(r)
        return flips


if __name__ == '__main__':
    solution = Solution()
    print(solution.pancakeSort([3, 2, 4, 1]))
    print(solution.pancakeSort([1, 2, 3]))

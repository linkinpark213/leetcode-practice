from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        AStar = [[0] * len(A) for _ in range(len(A[0]))]
        for i, row in enumerate(A):
            for j, num in enumerate(row):
                AStar[j][i] = num
        return AStar


if __name__ == '__main__':
    solution = Solution()
    print(solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution.transpose([[1, 2, 3], [4, 5, 6]]))

from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        distances = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        queue = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i, j, 0))

        while len(queue) > 0:
            i, j, dist = queue.pop(0)
            if distances[i][j] == -1:
                distances[i][j] = dist
                for m, n in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if m >= 0 and m < len(matrix) and n >= 0 and n < len(matrix[0]) and distances[m][n] < 0:
                        queue.append((m, n, dist + 1))
        return distances


if __name__ == '__main__':
    solution = Solution()
    print(solution.updateMatrix([[0, 0, 0],
                                 [0, 1, 0],
                                 [0, 0, 0]]))
    print(solution.updateMatrix([[0, 0, 0],
                                 [0, 1, 0],
                                 [1, 1, 1]]))

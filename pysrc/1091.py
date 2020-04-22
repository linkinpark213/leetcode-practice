from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dist = [[N * N + 1] * N for _ in range(N)]
        dist[N - 1][N - 1] = 1
        queue = [(N - 1, N - 1)] if grid[N - 1][N - 1] == 0 else []
        while len(queue) > 0:
            i, j = queue.pop(0)
            for k, l in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                         (i, j - 1), (i, j + 1),
                         (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                if k >= 0 and k < N and l >= 0 and l < N and grid[k][l] == 0 and dist[k][l] > dist[i][j] + 1:
                    dist[k][l] = dist[i][j] + 1
                    queue.append((k, l))
        return dist[0][0] if dist[0][0] <= N * N else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestPathBinaryMatrix([[0, 1],
                                             [1, 0]]))
    print(solution.shortestPathBinaryMatrix([[0, 0, 0],
                                             [1, 1, 0],
                                             [1, 1, 0]]))
    print(solution.shortestPathBinaryMatrix([[0, 0, 0],
                                             [1, 1, 0],
                                             [1, 1, 1]]))
    print(solution.shortestPathBinaryMatrix([[0, 1, 0, 0],
                                             [1, 0, 1, 0],
                                             [1, 1, 1, 0],
                                             [1, 1, 1, 0]]))

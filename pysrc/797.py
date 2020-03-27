from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        queue = [[0]]
        while len(queue) > 0:
            path = queue.pop()
            for next in graph[path[-1]]:
                newPath = path.copy()
                newPath.append(next)
                if next == len(graph) - 1:
                    ans.append(newPath)
                else:
                    queue.append(newPath)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.allPathsSourceTarget([[1, 2], [3], [3], []]))

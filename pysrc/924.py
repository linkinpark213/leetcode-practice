from typing import List


class Solution:
    def malwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        queue = initial.copy()
        infected = set(initial)
        while len(queue) > 0:
            node = queue.pop(0)
            for i, next in enumerate(graph[node]):
                if next == 1 and i != node and i not in infected:
                    infected.add(i)
                    queue.append(i)
        return len(infected)

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        minInfected = len(graph)
        initial.sort()
        nodeToRemove = initial[0]
        i = 0
        while i < len(initial):
            node = initial.pop(i)
            infected = self.malwareSpread(graph, initial)
            if minInfected > infected:
                nodeToRemove = node
                minInfected = infected
            initial.insert(i, node)
            i += 1
        return nodeToRemove


if __name__ == '__main__':
    solution = Solution()
    print(solution.minMalwareSpread(graph=[[1, 1, 0],
                                           [1, 1, 0],
                                           [0, 0, 1]], initial=[0, 1]))
    print(solution.minMalwareSpread(graph=[[1, 0, 0],
                                           [0, 1, 0],
                                           [0, 0, 1]], initial=[0, 2]))
    print(solution.minMalwareSpread(graph=[[1, 1, 1],
                                           [1, 1, 1],
                                           [1, 1, 1]], initial=[1, 2]))
    print(solution.minMalwareSpread(graph=[[1, 1, 0],
                                           [1, 1, 0],
                                           [0, 0, 1]], initial=[0, 1, 2]))
    print(solution.minMalwareSpread(graph=[[1, 0, 0, 0, 0, 0],
                                           [0, 1, 0, 0, 0, 0],
                                           [0, 0, 1, 0, 0, 0],
                                           [0, 0, 0, 1, 1, 0],
                                           [0, 0, 0, 1, 1, 0],
                                           [0, 0, 0, 0, 0, 1]], initial=[5, 0]))

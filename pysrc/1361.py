from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Find root
        nodes = set(range(n))
        roots = nodes.difference(set(leftChild)).difference(set(rightChild))
        if len(roots) != 1:
            return False
        root = iter(roots).__next__()
        parents = [-1] * n
        queue = [(root, -1)]
        while len(queue) > 0:
            node, parent = queue.pop()
            if node == -1:
                continue
            if parents[node] != -1:
                return False

            parents[node] = parent
            queue.append((leftChild[node], node))
            queue.append((rightChild[node], node))

        return parents.count(-1) == 1

if __name__ == '__main__':
    solution = Solution()
    print(solution.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]) == True)
    print(solution.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]) == False)
    print(solution.validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1]) == False)
    print(solution.validateBinaryTreeNodes(n=6, leftChild=[1, -1, -1, 4, -1, -1],
                                           rightChild=[2, -1, -1, 5, -1, -1]) == False)

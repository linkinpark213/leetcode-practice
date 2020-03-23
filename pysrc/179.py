from typing import List


class Node:
    def __init__(self, num):
        self.v = str(num)

    def __lt__(self, other):
        return self.v + other.v < other.v + self.v


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nodes = [Node(num) for num in nums]
        nodes.sort()
        nodes.reverse()

        ans = ''
        for node in nodes:
            ans += node.v
        while len(ans) > 1 and ans[0] == '0':
            ans = ans[1:]
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestNumber([10, 2]))
    print(solution.largestNumber([3, 30, 34, 5, 9]))
    print(solution.largestNumber([12, 121]))
    print(solution.largestNumber([0, 0]))
    print(solution.largestNumber([0]))

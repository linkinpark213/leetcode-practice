from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack = []
        for interval in intervals:
            if len(stack) == 0 or interval[0] > stack[-1][1]:
                stack.append(interval)
            else:
                stack[-1][1] = max(stack[-1][1], interval[1])

        return stack


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(solution.merge([[1, 4], [4, 5]]))

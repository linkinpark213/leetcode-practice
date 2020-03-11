from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        left = 0
        while left < len(intervals) and (intervals[left][1] < newInterval[0] or intervals[left][0] > newInterval[1]):
            left += 1

        right = 0
        while right < len(intervals) and intervals[right][0] <= newInterval[1]:
            right += 1

        mergedInterval = [0, 0]
        if left == len(intervals):
            mergedInterval[0] = newInterval[0]
        else:
            mergedInterval[0] = min(intervals[left][0], newInterval[0])

        if right == 0:
            mergedInterval[1] = newInterval[1]
        else:
            mergedInterval[1] = max(intervals[right - 1][1], newInterval[1])

        print('left = {}, right = {}'.format(left, right))

        if left < len(intervals) or right == len(intervals):
            for i in range(left, right):
                intervals.pop(left)
            intervals.insert(left, mergedInterval)
        elif left == len(intervals) and right < len(intervals):
            for i in range(left, right):
                intervals.pop(left)
            intervals.insert(right, mergedInterval)

        return intervals


if __name__ == '__main__':
    solution = Solution()
    print(solution.insert([[1, 3], [6, 9]], [2, 5]))
    print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(solution.insert([[1, 5]], [6, 8]))
    print(solution.insert([[1, 5]], [0, 3]))
    print(solution.insert([[1, 5]], [0, 1]))
    print(solution.insert([[1, 5]], [0, 0]))

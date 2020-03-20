from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        ends = []
        maxOccupied = 0
        for s, e in intervals:
            if len(ends) > 0:
                ends.sort()
                while len(ends) > 0 and ends[0] <= s:
                    ends.pop(0)
            ends.append(e)
            maxOccupied = max(maxOccupied, len(ends))

        return maxOccupied


if __name__ == '__main__':
    solution = Solution()
    print(solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print(solution.minMeetingRooms([[7, 10], [2, 4]]))
    print(solution.minMeetingRooms([[13, 15], [1, 13]]))

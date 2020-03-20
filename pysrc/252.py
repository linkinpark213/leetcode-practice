from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        free = 0
        for s, e in intervals:
            if s < free:
                return False
            free = e
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
    print(solution.canAttendMeetings([[7, 10], [2, 4]]))

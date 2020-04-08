from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) <= 1:
            return 0
        buckets = [[] for _ in range(24)]
        for time in timePoints:
            h, m = map(int, time.split(':'))
            buckets[h].append(m)

        minDifference = 1440
        for i in range(24):
            buckets[i].sort()
            for j in range(1, len(buckets[i])):
                minDifference = min(minDifference, buckets[i][j] - buckets[i][j - 1])

        prev = -1440
        for i in range(-23, 24):
            if len(buckets[i]) > 0:
                minDifference = min(minDifference, buckets[i][0] + 60 - prev)
                prev = buckets[i][-1]
            else:
                prev -= 60
        return minDifference


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findMinDifference(["23:59", "00:00"]))
    # print(solution.findMinDifference(["12:12", "00:13"]))
    print(solution.findMinDifference(["05:31", "22:08", "00:35"]))

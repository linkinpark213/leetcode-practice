from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        prev = [n + 1] * (n + 1)
        for i, r in enumerate(ranges):
            l, r = max(i - ranges[i], 0), min(i + ranges[i], n)
            prev[r] = min(prev[r], l)

        count = 0
        ptr = n
        while ptr > 0:
            jumpTo = ptr
            furthest = prev[jumpTo]
            for i in range(prev[ptr], ptr):
                if prev[i] < furthest:
                    furthest = prev[i]
                    jumpTo = i
                if i == 0:
                    return count + 1
            if furthest < prev[ptr]:
                ptr = jumpTo
                count += 1
            else:
                return -1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.minTaps(n=5, ranges=[3, 4, 1, 1, 0, 0]) == 1)
    print(solution.minTaps(n=3, ranges=[0, 0, 0, 0]) == -1)
    print(solution.minTaps(n=7, ranges=[1, 2, 1, 0, 2, 1, 0, 1]) == 3)
    print(solution.minTaps(n=8, ranges=[4, 0, 0, 0, 0, 0, 0, 0, 4]) == 2)
    print(solution.minTaps(n=8, ranges=[4, 0, 0, 0, 4, 0, 0, 0, 4]) == 1)

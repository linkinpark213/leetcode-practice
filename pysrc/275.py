from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i in range(1, len(citations) + 1):
            if citations[-i] < i:
                return i - 1
        return len(citations)


if __name__ == '__main__':
    solution = Solution()
    print(solution.hIndex([0, 1, 3, 5, 6]))
    print(solution.hIndex([0]))

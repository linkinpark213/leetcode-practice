from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = {}
        for citation in citations:
            if citation not in count.keys():
                count[citation] = 1
            else:
                count[citation] += 1

        sum = 0
        for citation in reversed(sorted(count.keys())):
            sum += count[citation]
            if citation < sum:
                return max(sum - count[citation], citation)
        return len(citations)


if __name__ == '__main__':
    solution = Solution()
    print(solution.hIndex([3, 0, 6, 1, 5]))
    print(solution.hIndex([0]))
    print(solution.hIndex([1, 1]))

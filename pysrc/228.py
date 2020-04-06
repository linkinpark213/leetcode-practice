from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        current = []
        for num in nums:
            if len(current) == 0 or len(current) > 0 and current[-1] + 1 == num:
                current.append(num)
            else:
                if len(current) > 1:
                    ranges.append('{}->{}'.format(current[0], current[-1]))
                    current = [num]
                elif len(current) == 1:
                    ranges.append('{}'.format(current[0]))
                    current = [num]
        if len(current) > 1:
            ranges.append('{}->{}'.format(current[0], current[-1]))
        elif len(current) == 1:
            ranges.append('{}'.format(current[0]))

        return ranges


if __name__ == '__main__':
    solution = Solution()
    print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))
    print(solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]))

from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        packs = list(zip(values, labels))
        packs.sort(key=lambda x: x[0], reverse=True)
        counters = {}
        i, sum, total = 0, 0, 0
        while total < num_wanted and i < len(packs):
            value, label = packs[i]
            if label not in counters:
                counters[label] = 1
            else:
                counters[label] += 1
            if counters[label] <= use_limit:
                sum += value
                total += 1
            i += 1
        return sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 1, 2, 2, 3], num_wanted=3, use_limit=1))
    print(solution.largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 3, 3, 3, 2], num_wanted=3, use_limit=2))
    print(solution.largestValsFromLabels(values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], num_wanted=3, use_limit=1))
    print(solution.largestValsFromLabels(values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], num_wanted=3, use_limit=2))

from typing import List


class Solution:
    def exchangeXYIfVertical(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> bool:
        if start1[0] == end1[0] or start2[0] == end2[0]:
            for point in [start1, end1, start2, end2]:
                temp = point[0]
                point[0] = point[1]
                point[1] = temp
            return True
        return False

    def exchangeSEIfRL(self, start: List[float], end: List[float]) -> bool:
        if start[0] > end[0]:
            temp = start.copy()
            start[0] = end[0]
            start[1] = end[1]
            end[0] = temp[0]
            end[1] = temp[1]
            return True
        return False

    def isHorizontal(self, start: List[int], end: List[int]) -> bool:
        return start[1] == end[1]

    def isVertical(self, start: List[int], end: List[int]) -> bool:
        return start[0] == end[0]

    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        xyExchanged = self.exchangeXYIfVertical(start1, end1, start2, end2)
        self.exchangeSEIfRL(start1, end1)
        self.exchangeSEIfRL(start2, end2)
        if self.isHorizontal(start1, end1) and self.isVertical(start2, end2):
            return [start2[0], end1[1]] if start1[0] < start2[0] and end1[0] > start2[0] else []
        elif self.isVertical(start1, end1) and self.isHorizontal(start2, end2):
            return [start1[0], end2[1]] if start2[0] < start1[0] and end2[0] > start1[0] else []

        k1 = (end1[1] - start1[1]) / (end1[0] - start1[0])
        k2 = (end2[1] - start2[1]) / (end2[0] - start2[0])

        l = max(start1[0], start2[0])
        r = min(end1[0], end2[0])

        if r < l - 10 ** -6:
            return []

        if k1 == k2:
            if (l - start1[0] == 0 and l > start2[0] or (k1 * (l - start1[0]) + start1[1]) == start2[1]) and (
                    l - start2[0] == 0 and l > start1[0] or (k2 * (l - start2[0]) + start2[1]) == start1[1]):
                return [k1 * (l - start1[0]) + start1[1], l] if xyExchanged else [l, k1 * (l - start1[0]) + start1[1]]
            else:
                return []

        if (k1 * (l - start1[0]) + start1[1]) - (k2 * (l - start2[0]) + start2[1]) == 0:
            return [k1 * (l - start1[0]) + start1[1], l] if xyExchanged else [l, k1 * (l - start1[0]) + start1[1]]
        if (k1 * (r - start1[0]) + start1[1]) - (k2 * (r - start2[0]) + start2[1]) == 0:
            return [k1 * (r - start1[0]) + start1[1], r] if xyExchanged else [r, k1 * (r - start1[0]) + start1[1]]

        while r - l > 10 ** -20:
            mid = (l + r) / 2
            if abs((k1 * (mid - start1[0]) + start1[1]) - (k2 * (mid - start2[0]) + start2[1])) < 10 ** -6:
                return [k1 * (mid - start1[0]) + start1[1], mid] if xyExchanged else [mid,
                                                                                      k1 * (mid - start1[0]) + start1[
                                                                                          1]]
            elif ((k1 * (mid - start1[0]) + start1[1]) - (k2 * (mid - start2[0]) + start2[1])) * (
                    (k1 * (l - start1[0]) + start1[1]) - (k2 * (l - start2[0]) + start2[1])) < 0:
                r = mid
            else:
                l = mid

        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.intersection([0, 0], [1, 0], [1, 1], [0, -1]))
    print(solution.intersection([0, 0], [3, 3], [1, 1], [2, 2]))
    print(solution.intersection([0, 0], [1, 1], [1, 0], [2, 1]))
    print(solution.intersection([0, 0], [5, 0], [3, 4], [3, -2]))
    print(solution.intersection([0, 0], [0, 1], [1, 0], [1, 1]))
    print(solution.intersection([0, 0], [0, 1], [0, 2], [0, 3]))
    print(solution.intersection([1, 0], [1, 1], [-1, 0], [3, 2]))
    print(solution.intersection([-1, 1], [1, 1], [-3, 2], [1, 0]))

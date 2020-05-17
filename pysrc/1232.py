from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        [x0, y0], [x1, y1] = coordinates[0], coordinates[1]
        for (x, y) in coordinates[2:]:
            if y != y0 and y != y1:
                if (x - x0) / (y - y0) != (x - x1) / (y - y1):
                    return False
            elif x != x0 and x != x1:
                if (y - y0) / (x - x0) != (y - y1) / (x - x1):
                    return False
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkStraightLine(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(solution.checkStraightLine(coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
    print(solution.checkStraightLine(coordinates=[[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]]))

from typing import List


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Sea(object):
    def __init__(self, ships: List[Point]):
        self.ships = ships
        self.count = 0

    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        self.count += 1
        for ship in self.ships:
            if ship.x <= topRight.x and ship.y <= topRight.y and ship.x >= bottomLeft.x and ship.y >= bottomLeft.y:
                return True
        return False


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1 if sea.hasShips(topRight, bottomLeft) else 0
        elif topRight.x >= bottomLeft.x and topRight.y >= bottomLeft.y:
            if not sea.hasShips(topRight, bottomLeft):
                return 0
            midX, midY = (topRight.x + bottomLeft.x) // 2, (topRight.y + bottomLeft.y) // 2
            ans = self.countShips(sea, Point(midX, midY), bottomLeft)
            ans += self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1))
            ans += self.countShips(sea, topRight, Point(midX + 1, midY + 1))
            ans += self.countShips(sea, Point(topRight.x, midY), Point(midX + 1, bottomLeft.y))
            return ans
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    sea = Sea([Point(1, 1), Point(2, 2), Point(3, 3), Point(5, 5)])
    print(solution.countShips(sea, Point(4, 4), Point(0, 0)))

    sea = Sea([Point(6, 6), Point(100, 50), Point(999, 81), Point(50, 50), Point(700, 600)])
    print(solution.countShips(sea, Point(1000, 1000), Point(0, 0)))

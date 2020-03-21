from typing import List


class Solution:
    def measurables(self, x: int, y: int) -> List[bool]:
        count = [False] * (x + y + 1)
        stack = [0]
        while len(stack) > 0:
            v = stack.pop()
            for newV in [abs(v - x), abs(v - y), min(v + x, x + y), min(v + y, x + y)]:
                if not count[newV]:
                    count[newV] = True
                    stack.append(newV)
        return count

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z < 0 or z > x + y:
            return False
        return self.measurables(x, y)[z]


if __name__ == '__main__':
    solution = Solution()
    print(solution.canMeasureWater(x=3, y=5, z=4))
    print(solution.canMeasureWater(x=2, y=6, z=5))

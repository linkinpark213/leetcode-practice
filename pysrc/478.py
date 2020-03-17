import math
import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        r = (random.random() ** 0.5) * self.radius
        theta = random.uniform(0, 2 * math.pi)
        return [r * math.cos(theta) + self.x_center, r * math.sin(theta) + self.y_center]


if __name__ == '__main__':
    # Your Solution object will be instantiated and called as such:
    radius, x_center, y_center = 0.01, -73839.1, -3289891.3
    obj = Solution(radius, x_center, y_center)
    for i in range(1000000):
        x, y = obj.randPoint()
        if (x - x_center) ** 2 + (y - y_center) ** 2 == radius ** 2:
            print('{}^2 + {}^2 == {}^2'.format(x - x_center, y - y_center, radius))

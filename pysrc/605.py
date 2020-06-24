from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        nZeros = 0
        canPlant = 0
        flowerbed = [0] + flowerbed + [0, 1]
        for num in flowerbed:
            if num == 1:
                canPlant += self.plant(nZeros)
                nZeros = 0
            else:
                nZeros += 1
        return canPlant >= n

    def plant(self, nZeros):
        return (nZeros - 1) // 2 if nZeros > 2 else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
    print(solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))

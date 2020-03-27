from typing import List


class Solution:
    def helper(self, d, i):
        for k in d.keys():
            if d[k] % i != 0:
                return False
        return True

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = {}
        for card in deck:
            if card in d.keys():
                d[card] += 1
            else:
                d[card] = 1

        for i in range(2, min(d.values()) + 1):
            if self.helper(d, i):
                return True
            continue
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
    print(solution.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
    print(solution.hasGroupsSizeX([1]))
    print(solution.hasGroupsSizeX([1, 1]))
    print(solution.hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
    print(solution.hasGroupsSizeX([0, 0, 0, 1, 1, 1, 2, 2, 2]))

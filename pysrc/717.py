from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if i == len(bits) - 1:
                return True
            if bits[i] == 1:
                i += 1
            i += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isOneBitCharacter([1, 0, 0]))
    print(solution.isOneBitCharacter([1, 1, 1, 0]))
    print(solution.isOneBitCharacter([0, 1, 0]))

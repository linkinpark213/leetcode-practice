from typing import List


class Solution:
    def position(self, c: str) -> List[int]:
        asc = ord(c) - ord('a')
        return [asc // 5, asc % 5]

    def movement2str(self, move: List[int], horizontalFirst: bool = True) -> str:
        horizontal = ('D' if move[0] > 0 else 'U') * abs(move[0])
        vertical = ('R' if move[1] > 0 else 'L') * abs(move[1])
        return (horizontal + vertical if horizontalFirst else vertical + horizontal) + '!'

    def alphabetBoardPath(self, target: str) -> str:
        pos = [0, 0]
        ans = ''
        for c in target:
            newPos = self.position(c)
            move = [newPos[0] - pos[0], newPos[1] - pos[1]]
            ans += self.movement2str(move, c != 'z')
            pos = newPos
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.alphabetBoardPath('leet'))
    print(solution.alphabetBoardPath('code'))

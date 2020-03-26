from typing import List


class Solution:
    def findRook(self, board: List[List[str]]) -> (int, int):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return i, j

    def captureInRange(self, board: List[List[str]], iRange: range, jRange: range) -> int:
        for i in iRange:
            for j in jRange:
                if board[i][j] == 'p':
                    return 1
                elif board[i][j] == 'B':
                    return 0
        return 0

    def numRookCaptures(self, board: List[List[str]]) -> int:
        rookI, rookJ = self.findRook(board)
        count = 0
        for iRange, jRange in [((rookI, -1, -1), (rookJ, rookJ + 1)), ((rookI, 8), (rookJ, rookJ + 1)),
                               ((rookI, rookI + 1), (rookJ, -1, -1)), ((rookI, rookI + 1), (rookJ, 8))]:
            count += self.captureInRange(board, range(*iRange), range(*jRange))
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."],
                                    [".", ".", ".", "p", ".", ".", ".", "."],
                                    [".", ".", ".", "R", ".", ".", ".", "p"],
                                    [".", ".", ".", ".", ".", ".", ".", "."],
                                    [".", ".", ".", ".", ".", ".", ".", "."],
                                    [".", ".", ".", "p", ".", ".", ".", "."],
                                    [".", ".", ".", ".", ".", ".", ".", "."],
                                    [".", ".", ".", ".", ".", ".", ".", "."]]))
    print(solution.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."],
                                    [".", "p", "p", "p", "p", "p", ".", "."],
                                    [".", "p", "p", "B", "p", "p", ".", "."],
                                    [".", "p", "B", "R", "B", "p", ".", "."],
                                    [".", "p", "p", "B", "p", "p", ".", "."],
                                    [".", "p", "p", "p", "p", "p", ".", "."],
                                    [".", ".", ".", ".", ".", ".", ".", "."],
                                    [".", ".", ".", ".", ".", ".", ".", "."]]))

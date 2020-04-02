from typing import List


class Solution:
    states = [0, 1, 1, 0]
    transitions = [[0, 0, 0, -2, 0, 0, 0, 0, 0], [-1, -1, 1, 1, -1, -1, -1, -1, -1]]

    def countSurroundingAlive(self, board: List[List[int]], i: int, j: int) -> int:
        count = -board[i][j]
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if i + di >= 0 and i + di < len(board) and j + dj >= 0 and j + dj < len(board[0]):
                    count += 1 if abs(board[i + di][j + dj]) == 1 else 0
        return count

    def stateSimplify(self, board: List[List[int]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = self.states[board[i][j]]

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                alive = self.countSurroundingAlive(board, i, j)
                board[i][j] = self.transitions[board[i][j]][alive]
        self.stateSimplify(board)


if __name__ == '__main__':
    solution = Solution()
    print(solution.gameOfLife([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]))

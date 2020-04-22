from typing import List


class Solution:
    def dfs(self, board: List[List[str]], word: str, path: List[List[int]]) -> bool:
        if len(path) == len(word):
            return True
        i, j = path[-1]
        for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if k >= 0 and k < len(board) and l >= 0 and l < len(board[0]) and \
                    board[k][l] == word[len(path)] and [k, l] not in path and self.dfs(board, word, path + [[k, l]]):
                return True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.dfs(board, word, [[i, j]]):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.exist(board=[["A", "B", "C", "E"],
                                ["S", "F", "C", "S"],
                                ["A", "D", "E", "E"]],
                         word="ABCCED"))
    print(solution.exist(board=[["a", "b"], ["c", "d"]],
                         word="abcd"))

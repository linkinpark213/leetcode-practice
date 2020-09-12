from typing import List


class Solution:
    def find(self, board: List[List[str]], word: str, path: List):
        if len(word) == 0:
            return True

        m, n = len(board), len(board[0])
        i, j = path[-1]
        for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if k >= 0 and k < m and l >= 0 and l < n and (k, l) not in path and board[k][l] == word[0]:
                path.append((k, l))
                if self.find(board, word[1:], path):
                    return True
                path.pop()
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.find(board, word[1:], [(i, j)]):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(solution.exist(board, 'ABCCED') == True)
    print(solution.exist(board, 'SEE') == True)
    print(solution.exist(board, 'ABCB') == False)

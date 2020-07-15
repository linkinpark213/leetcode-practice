from typing import List


class TrieNode:
    def __init__(self, c):
        self.c = c
        self.paths = []
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def search(self, word, board):
        ptr = self.root
        for i, c in enumerate(word):
            if c not in ptr.children.keys():
                ptr.children[c] = TrieNode(c)
                if (i == 0):
                    ptr.children[c].Y = findChar(board, c)
                else:
                    for path in ptr.paths:
                        ptr.children[c].Y.extend(findChar(board, c, path))

            ptr = ptr.children[c]
            if len(ptr.Y) == 0:
                return False
        return True


def findChar(board: List[List[str]], c: str, path_from: List = None):
    height, width = len(board), len(board[0])
    paths = []
    if path_from is None:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == c:
                    paths.append([(row, col)])
    else:
        row, col = path_from[-1]
        for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if i >= 0 and i < height and j >= 0 and j < width and (i, j) not in path_from and board[i][j] == c:
                paths.append(path_from.copy() + [(i, j)])
    return paths


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        existence = [word for word in words if trie.search(word, board)]
        return existence


if __name__ == '__main__':
    solution = Solution()
    print(solution.findWords([['o', 'a', 'a', 'n'],
                              ['e', 't', 'a', 'e'],
                              ['i', 'h', 'k', 'r'],
                              ['i', 'f', 'l', 'v']],
                             ["oath", "pea", "eat", "rain"]))
    print(solution.findWords([['a']],
                             ["a"]))

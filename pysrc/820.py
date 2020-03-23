from typing import List


class TrieNode:
    def __init__(self, depth):
        self.depth = depth
        self.children = {}

    def save(self, word):
        if len(word) > 0:
            if word[-1] not in self.children.keys():
                self.children[word[-1]] = TrieNode(self.depth + 1)
            self.children[word[-1]].save(word[:-1])

    def count(self):
        sum = 0
        for k, v in self.children.items():
            sum += v.count()
        return max(self.depth + 1, sum)


class Solution:
    def minimumLengthEncoding(self, words: List[str]):
        trie = TrieNode(0)
        for word in words:
            trie.save(word)
        return trie.count()


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumLengthEncoding(['time', 'me', 'bell']))

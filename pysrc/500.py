from typing import List


class Solution:
    groups = [1, 2, 2, 1, 0, 1, 1, 1, 0, 1, 1, 1, 2, 2, 0, 0, 0, 0, 1, 0, 0, 2, 0, 2, 0, 2]

    def wordOK(self, word: str) -> bool:
        line = -1
        for c in word.upper():
            if line != -1 and line != self.groups[ord(c) - ord('A')]:
                return False
            line = self.groups[ord(c) - ord('A')]
        return True

    def findWords(self, words: List[str]) -> List[str]:
        return [word for word in words if self.wordOK(word)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))

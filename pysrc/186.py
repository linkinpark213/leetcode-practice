from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr = 0
        wordLength = 0
        for i in range(len(s)):
            c = s.pop()
            if c == ' ':
                ptr = ptr + wordLength
                s.insert(ptr, c)
                ptr += 1
                wordLength = 0
            else:
                s.insert(ptr, c)
                wordLength += 1
        return


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords(["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]))

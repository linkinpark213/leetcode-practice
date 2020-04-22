from typing import List


class Solution:
    def find(self, s: str, w: str) -> bool:
        ptr = 0
        for c in s:
            if c == w[ptr]:
                ptr += 1
            if ptr == len(w):
                return True
        return False

    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort()
        d.sort(key=len, reverse=True)
        for w in d:
            if self.find(s, w):
                return w
        return ''


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLongestWord(s="abpcplea", d=["ale", "apple", "monkey", "plea"]))
    print(solution.findLongestWord(s="abpcplea", d=["a", "b", "c"]))

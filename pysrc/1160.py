from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for c in chars:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1

        count = 0
        for word in words:
            available = d.copy()
            for i, c in enumerate(word):
                if c not in available.keys() or available[c] == 0:
                    break
                else:
                    available[c] -= 1
                    if i == len(word) - 1:
                        count += len(word)
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
    print(solution.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))

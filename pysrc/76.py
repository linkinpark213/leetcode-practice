class Solution:
    def contains(self, counts, letters):
        for n1, n2 in zip(counts, letters):
            if n1 < n2:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        pos, letters = {}, []
        i = 0
        for c in t:
            if c not in pos:
                pos[c] = i
                letters.append(1)
                i += 1
            else:
                letters[pos[c]] += 1

        counts = [0] * len(pos)
        minLength, minL, minR = len(s), 0, 0
        l, r = 0, 0
        while r <= len(s) or l < r:
            if self.contains(counts, letters):
                if r - l <= minLength:
                    minLength, minL, minR = r - l, l, r
                if s[l] in pos:
                    counts[pos[s[l]]] = max(counts[pos[s[l]]] - 1, 0)
                l += 1
            elif r < len(s):
                if s[r] in pos:
                    counts[pos[s[r]]] += 1
                r += 1
            else:
                break
        return s[minL: minR]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))
    print(solution.minWindow(s="a", t="a"))
    print(solution.minWindow(s="a", t="aa"))

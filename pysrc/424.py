class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def index(c):
            return ord(c) - ord('A')

        if len(s) == 0:
            return 0
        counts = [0] * 26
        l, r = 0, 0
        ans = k
        counts[index(s[0])] = 1
        while r < len(s):
            if r - l + 1 < max(counts) + k or (
                    r - l + 1 == max(counts) + k and r < len(s) - 1 and counts[index(s[r + 1])] == max(counts)):
                r += 1
                if r == len(s):
                    return max(r - l, ans)
                ans = max(ans, r - l + 1)
                counts[index(s[r])] += 1
            elif r - l + 1 == max(counts) + k:
                counts[index(s[l])] -= 1
                l += 1
                r += 1
                if r != len(s):
                    counts[index(s[r])] += 1
            else:
                counts[index(s[l])] -= 1
                l += 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.characterReplacement(s="ABAB", k=2))
    print(solution.characterReplacement(s="AABABBA", k=1))
    print(solution.characterReplacement(s="AAAA", k=1))
    print(solution.characterReplacement(s="AAAA", k=0))
    print(solution.characterReplacement(s="ABAA", k=0))
    print(solution.characterReplacement(
        s="IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR",
        k=2))

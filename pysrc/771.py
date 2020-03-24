class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([S.count(c) for c in J])


if __name__ == '__main__':
    solution = Solution()
    print(solution.numJewelsInStones(J="aA", S="aAAbbbb"))
    print(solution.numJewelsInStones(J="z", S="ZZ"))

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) | (n & 1)
            n = n >> 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(43261596) == 964176192)
    print(solution.reverseBits(4294967293) == 3221225471)

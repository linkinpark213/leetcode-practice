class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        sum = 0
        z = x ^ y
        while z != 0:
            sum += z & 1
            z = z >> 1
        return sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingDistance(1, 4))

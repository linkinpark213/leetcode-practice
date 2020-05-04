class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 1:
            return 1
        ans = 1
        while ans * ans <= n:
            ans += 1
        return ans - 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.bulbSwitch(3))
    print(solution.bulbSwitch(4))

class Solution:
    @staticmethod
    def transform(n: int) -> int:
        ans = 0
        while n > 0:
            ans += (n % 10) ** 2
            n = n // 10
        return ans

    def isHappy(self, n: int) -> bool:
        history = [n]
        while True:
            n = self.transform(n)
            if n == 1:
                return True
            elif n in history:
                return False
            history.append(n)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(19))

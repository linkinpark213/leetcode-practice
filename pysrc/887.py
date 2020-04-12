class Solution:
    def dp(self, k, n, memo):
        if (k, n) not in memo:
            if n == 0:
                ans = 0
            elif k == 1:
                ans = n
            else:
                l, r = 1, n
                while l + 1 < r:
                    x = (l + r) // 2
                    t1 = self.dp(k - 1, x - 1, memo)
                    t2 = self.dp(k, n - x, memo)

                    if t1 < t2:
                        l = x
                    elif t1 > t2:
                        r = x
                    else:
                        l = r = x

                ans = 1 + min(max(self.dp(k - 1, x - 1, memo), self.dp(k, n - x, memo))
                              for x in (l, r))

            memo[k, n] = ans
        return memo[k, n]

    def superEggDrop(self, K: int, N: int) -> int:
        return self.dp(K, N, {})


if __name__ == '__main__':
    solution = Solution()
    print(solution.superEggDrop(K=1, N=2))
    print(solution.superEggDrop(K=2, N=6))
    print(solution.superEggDrop(K=3, N=14))

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2, n):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        return sum(isPrime)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(10))
    print(solution.countPrimes(2))

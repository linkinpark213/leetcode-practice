class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        i = 1
        count = 1
        while i ** 2 <= 2 * N:
            i = i + 1
            temp = N - i * (i + 1) // 2
            if temp >= 0 and temp % i == 0:
                count += 1
                print(i, end=', ')
        print(count)
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.consecutiveNumbersSum(1) == 1)
    print(solution.consecutiveNumbersSum(3) == 2)
    print(solution.consecutiveNumbersSum(4) == 1)
    print(solution.consecutiveNumbersSum(5) == 2)
    print(solution.consecutiveNumbersSum(9) == 3)
    print(solution.consecutiveNumbersSum(15) == 4)
    print(solution.consecutiveNumbersSum(85) == 4)

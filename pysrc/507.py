class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        i = 2
        sum = 1
        while i ** 2 < num:
            if num % i == 0:
                sum += i + num // i
            i += 1
        if i ** 2 == num:
            sum += i
        return sum == num


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPerfectNumber(28))

class Solution:
    values = [1000, 500, 100, 50, 10, 5, 1]
    symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    def intToRoman(self, num: int) -> str:
        s = ''
        for i in range(len(self.values)):
            d = num // self.values[i]
            num -= d * self.values[i]
            if d <= 3:
                s += self.symbols[i] * d
            elif d == 4:
                if len(s) == 0 or s[-1] != self.symbols[i - 1]:
                    s += self.symbols[i] + self.symbols[i - 1]
                else:
                    s = s[:-1]
                    s += self.symbols[i] + self.symbols[i - 2]

        return s


if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(3))
    print(solution.intToRoman(4))
    print(solution.intToRoman(9))
    print(solution.intToRoman(58))
    print(solution.intToRoman(1994))

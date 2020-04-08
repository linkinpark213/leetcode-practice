class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s = ''
        p1, p2 = len(num1) - 1, len(num2) - 1
        carry = 0
        while p1 >= 0 or p2 >= 0:
            digit = (int(num1[p1]) if p1 >= 0 else 0) + (int(num2[p2]) if p2 >= 0 else 0) + carry
            carry = digit // 10
            digit = digit % 10
            s = str(digit) + s
            p1 -= 1
            p2 -= 1
        if carry > 0:
            s = str(carry) + s
        return s


if __name__ == '__main__':
    solution = Solution()
    print(solution.addStrings('12345', '56789'))

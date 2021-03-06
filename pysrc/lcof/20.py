class Solution:
    def __init__(self):
        # 0 - start  1 - symbol  2 - beforeDot  3 - dotAfterInt  4 - dotAlone
        # 5 - afterDot  6 - expo  7 - expoSymbol  8 - expoInt  9 - space
        self.isFinal = [False, False, True, True, False, True, False, False, True, True]
        self.nexts = [
            [
                ((lambda x: x in ['+', '-'], 1)),
                (lambda x: ord(x) >= ord('0') and ord(x) <= ord(('9')), 2),
                (lambda x: x == '.', 4),
                (lambda x: x == ' ', 0)
            ], [
                (lambda x: ord(x) >= ord('0') and ord(x) <= ord(('9')), 2),
                (lambda x: x == '.', 4)
            ], [
                (lambda x: ord(x) >= ord('0') and ord(x) <= ord(('9')), 2),
                (lambda x: x == 'e', 6),
                (lambda x: x == '.', 3),
                (lambda x: x == ' ', 9)
            ], [
                (lambda x: ord(x) >= ord('0') and ord(x) <= ord(('9')), 5),
                (lambda x: x == 'e', 6),
                (lambda x: x == ' ', 9)
            ], [
                (lambda x: ord(x) >= ord('0') and ord(x) <= ord(('9')), 5),
            ], [
                (lambda x: ord(x) >= ord('0') and ord(x) <= ord(('9')), 5),
                (lambda x: x == 'e', 6),
                (lambda x: x == ' ', 9),
            ], [
                (lambda x: x in ['+', '-'], 7),
                (lambda x: ord(x) >= ord('0') and ord(x) <= ord(('9')), 8)
            ], [
                (lambda x: ord(x) >= ord('0') and ord(x) <= ord(('9')), 8)
            ], [
                (lambda x: ord(x) >= ord('0') and ord(x) <= ord(('9')), 8),
                (lambda x: x == ' ', 9)
            ], [
                (lambda x: x == ' ', 9)
            ]
        ]

    def next(self, state, c):
        for func, state in self.nexts[state]:
            if func(c):
                return state
        return -1

    def isNumber(self, s: str) -> bool:
        state = 0
        ptr = 0
        while ptr < len(s):
            state = self.next(state, s[ptr])
            if state < 0:
                return False
            ptr += 1
        return ptr == len(s) and self.isFinal[state]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isNumber("+100"))
    print(solution.isNumber("5e2"))
    print(solution.isNumber("-123"))
    print(solution.isNumber("3.1416"))
    print(solution.isNumber("0123"))
    print(not solution.isNumber("12e"))
    print(not solution.isNumber("1a3.14"))
    print(not solution.isNumber("1.2.3"))
    print(not solution.isNumber("+-5"))
    print(not solution.isNumber("-1E-16"))
    print(not solution.isNumber("12e+5.4"))
    print(solution.isNumber("1 "))
    print(not solution.isNumber("e9"))
    print(solution.isNumber('1.'))
    print(solution.isNumber('.1'))
    print(not solution.isNumber('.'))
    print(solution.isNumber('005047e+6'))

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0
        for i, c in enumerate(s1):
            if c == 'x' and s2[i] == 'y':
                xy += 1
            elif c == 'y' and s2[i] == 'x':
                yx += 1

        if (xy + yx) % 2 > 0:
            return -1

        return xy % 2 + yx % 2 + xy // 2 + yx // 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumSwap('xx', 'yy'))
    print(solution.minimumSwap('xy', 'yx'))
    print(solution.minimumSwap('xx', 'xy'))
    print(solution.minimumSwap('xxyyxyxyxx', 'xyyxyxxxyx'))

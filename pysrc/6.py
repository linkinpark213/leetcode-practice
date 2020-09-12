class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        direction = -1
        pos = 0
        parts = ['' for _ in range(numRows)]
        for c in s:
            parts[pos] += c

            if pos == 0 or pos == numRows - 1:
                direction = -direction

            pos = pos + direction
        return ''.join(parts)


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert(s="LEETCODEISHIRING", numRows=3) == "LCIRETOESIIGEDHN")
    print(solution.convert(s="LEETCODEISHIRING", numRows=4) == "LDREOEIIECIHNTSG")

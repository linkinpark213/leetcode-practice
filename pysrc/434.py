class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        buffer = 0
        for c in s:
            if c == ' ' and buffer > 0:
                count += 1
                buffer = 0
            elif c != ' ':
                buffer += 1
        if buffer > 0:
            count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.countSegments("Hello, my name is John"))
    print(solution.countSegments("                "))

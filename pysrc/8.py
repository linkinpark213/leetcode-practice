class Solution:
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    def myAtoi(self, str: str) -> int:
        sign = 1
        ans = 0
        ptr = 0
        while ptr < len(str) and str[ptr] == ' ':
            ptr += 1

        if ptr < len(str):
            if str[ptr] == '-':
                sign = -1
                ptr += 1
            elif str[ptr] == '+':
                ptr += 1

            while ptr < len(str):
                if str[ptr] >= '0' and str[ptr] <= '9':
                    ans = ans * 10 + ord(str[ptr]) - ord('0')
                    ptr += 1
                else:
                    break

        return max(min(ans * sign, self.INT_MAX), self.INT_MIN)


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi("42"))
    print(solution.myAtoi("    -42"))
    print(solution.myAtoi("4193 with words"))
    print(solution.myAtoi("words and 987"))
    print(solution.myAtoi("-91283472332"))

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        repeat = 0
        for c in s:
            if c == ']':
                pat = ''
                while True:
                    if type(stack[-1]) is not int:
                        pat = stack.pop() + pat
                    else:
                        stack.append(pat * stack.pop())
                        break
            elif c == '[':
                stack.append(repeat)
                repeat = 0
            elif c >= '0' and c <= '9':
                repeat = repeat * 10 + int(c)
            else:
                stack.append(c)
        ans = ''
        for s in stack:
            ans += s
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString(s="3[a]2[bc]"))
    print(solution.decodeString(s="3[a2[c]]"))
    print(solution.decodeString(s="2[abc]3[cd]ef"))
    print(solution.decodeString(s="100[leetcode]"))

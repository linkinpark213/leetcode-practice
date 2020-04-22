class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        maxLength = 0
        for i, c in enumerate(s):
            maxLength = max(maxLength, i - stack[-1][0] - 1 if len(stack) > 0 else i)
            if c == '(':
                if len(stack) == 0:
                    maxLength = max(maxLength, i)
                stack.append((i, c))
            elif c == ')':
                if len(stack) > 0 and stack[-1][1] == '(':
                    if stack[-1][1] == '(':
                        stack.pop()
                else:
                    stack.append((i, c))

        return max(maxLength, len(s) - stack[-1][0] - 1 if len(stack) > 0 else len(s))


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestValidParentheses("(()"))
    print(solution.longestValidParentheses(")()())"))
    print(solution.longestValidParentheses("()(()"))
    print(solution.longestValidParentheses("(())()(()(("))
    print(solution.longestValidParentheses(")("))
    print(solution.longestValidParentheses("())"))

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for token in path.split('/'):
            if len(token) == 0 or token == '.':
                continue
            if token == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(token)

        if len(stack) == 0:
            return '/'
        s = ''
        for token in stack:
            s += '/' + token
        return s


if __name__ == '__main__':
    solution = Solution()
    print(solution.simplifyPath("/home/"))
    print(solution.simplifyPath("/../"))
    print(solution.simplifyPath("/home//foo/"))
    print(solution.simplifyPath("/a/./b/../../c/"))
    print(solution.simplifyPath("/a/../../b/../c//.//"))
    print(solution.simplifyPath("/a//b////c/d//././/.."))

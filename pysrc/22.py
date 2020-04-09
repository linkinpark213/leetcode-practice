from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        elif n == 1:
            return ['()']
        queue = [(1, '(')]
        ans = []
        while len(queue) > 0:
            depth, s = queue.pop(0)
            if depth == 0 and len(s) == n * 2:
                ans.append(s)
            else:
                if depth > 0:
                    queue.append((depth - 1, s + ')'))
                if len(s) + depth < n * 2:
                    queue.append((depth + 1, s + '('))
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(n=2))
    print(solution.generateParenthesis(n=3))
    print(solution.generateParenthesis(n=4))

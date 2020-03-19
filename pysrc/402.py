class Solution:
    def selectDigits(self, num: str, k: int):
        stack = []
        toDelete = []
        for i, c in enumerate(num):
            while len(stack) > 0 and int(num[stack[-1]]) > int(c):
                toDelete.append(stack.pop())
                if len(toDelete) == k:
                    return toDelete
            stack.append(i)

        if len(toDelete) < k:
            toDelete.extend(stack[-(k - len(toDelete)):])

        return toDelete

    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'

        toDelete = self.selectDigits(num, k)
        print(toDelete)

        ans = ''
        for i, c in enumerate(num):
            if i not in toDelete:
                ans += c
        while len(ans) > 0 and ans[0] == '0':
            ans = ans[1:]
        if len(ans) == 0:
            ans = '0'
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeKdigits('1432219', 3))
    print(solution.removeKdigits('10200', 1))
    print(solution.removeKdigits('10', 1))
    print(solution.removeKdigits('112', 1))
    print(solution.removeKdigits('1111111', 3))
    print(solution.removeKdigits('1234567890', 9))

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for num in pushed:
            stack.append(num)
            while len(stack) > 0 and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return len(popped) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
    print(solution.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))

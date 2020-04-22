from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if numbers[-1] > numbers[0]:
            return numbers[0]
        minValue = numbers[-1]
        ptr = len(numbers) - 1
        while ptr >= 0:
            ptr -= 1
            if numbers[ptr] <= minValue:
                minValue = numbers[ptr]
            else:
                break
        return minValue


if __name__ == '__main__':
    solution = Solution()
    print(solution.minArray([3, 4, 5, 1, 2]))
    print(solution.minArray([2, 2, 2, 0, 1]))

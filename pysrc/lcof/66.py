from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        left, right = [1], [1]
        for num in a:
            left.append(num * left[-1])
        for num in a[::-1]:
            right.insert(0, num * right[0])
        return [left[i] * right[i + 1] for i in range(len(a))]


if __name__ == '__main__':
    solution = Solution()
    print(solution.constructArr([1, 2, 3, 4, 5]))

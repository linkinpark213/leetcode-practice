from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        d = {}
        for num in A:
            if num not in d.keys():
                d[num] = 1
            else:
                d[num] += 1

        ptr, top = min(d.keys()), max(d.keys())
        accumulate = 0
        newSum = 0
        while ptr <= top or accumulate > 0:
            if ptr not in d.keys():
                if accumulate > 0:
                    newSum += ptr
                accumulate = max(0, accumulate - 1)
            else:
                accumulate += d[ptr] - 1
                newSum += ptr
            ptr += 1
        return newSum - sum(A)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minIncrementForUnique([1, 2, 2]))
    print(solution.minIncrementForUnique([3, 2, 1, 2, 1, 7]))

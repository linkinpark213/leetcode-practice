from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i = 2
        sequences = []
        while (i * (i - 1) / 2 < target):
            temp = target - (i - 1) * i / 2
            if (temp % i == 0):
                n1 = int(temp // i)
                sequences.insert(0, list(range(n1, n1 + i)))
            i += 1

        return sequences


if __name__ == '__main__':
    solution = Solution()
    print(solution.findContinuousSequence(1))
    print(solution.findContinuousSequence(9))
    print(solution.findContinuousSequence(15))

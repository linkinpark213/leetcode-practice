from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        neg, pos = [num for num in A if num < 0], [num for num in A if num >= 0]
        neg.sort()
        pos.sort()
        if len(neg) >= K:
            return sum(pos) + sum([-num for num in neg[:K]]) + sum([num for num in neg[K:]])
        elif (K - len(neg)) % 2 == 0:
            return sum(pos) - sum(neg)
        else:
            if len(pos) > 0 and len(neg) > 0:
                return sum(pos[1:]) - sum(neg[:-1]) + max(abs(neg[-1]), abs(pos[0])) - min(abs(neg[-1]), abs(pos[0]))
            elif len(pos) == 0:
                return -sum(neg) + 2 * neg[-1]
            elif len(neg) == 0:
                return sum(pos) - 2 * pos[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestSumAfterKNegations(A=[4, 2, 3], K=1) == 5)
    print(solution.largestSumAfterKNegations(A=[3, -1, 0, 2], K=3) == 6)
    print(solution.largestSumAfterKNegations(A=[2, -3, -1, 5, -4], K=2) == 13)
    print(solution.largestSumAfterKNegations(A=[-8, 3, -5, -3, -5, -2], K=6) == 22)

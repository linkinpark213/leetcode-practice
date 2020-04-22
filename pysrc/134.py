from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        remains = [gas[i] - cost[i] for i in range(N)]
        if sum(remains) < 0:
            return -1
        elif len(remains) == 1:
            return 0
        for i in range(N):
            if remains[i] > 0 and remains[i - 1] <= 0:
                s = remains[i]
                for j in range(1, N):
                    s += remains[(i + j) % N]
                    if s < 0:
                        break
                    elif j == N - 1:
                        return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    print(solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))

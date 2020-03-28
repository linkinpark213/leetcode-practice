from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = {0: [[]]}
        for num in candidates:
            newDp = {k: v.copy() for k, v in dp.items()}
            for k in dp.keys():
                if k + num <= target:
                    if k + num not in newDp.keys():
                        newDp[k + num] = []
                    for path in dp[k]:
                        newPath = sorted(path + [num])
                        if newPath not in newDp[k + num]:
                            newDp[k + num].append(newPath)
            dp = newDp

        return dp[target] if target in dp.keys() else []


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
    print(solution.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
    print(solution.combinationSum2(candidates=[2], target=1))
    print(solution.combinationSum2(candidates=[1, 5, 2, 3, 1, 5, 1, 2, 4, 1, 4], target=3))

from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [0] * len(arr)
        positions = [(i, num) for i, num in enumerate(arr)]
        positions.sort(key=lambda x: x[1])
        for pos, num in positions:
            dp[pos] = 1
            for r in [range(pos - 1, max(0, pos - d) - 1, -1), range(pos + 1, min(len(arr), pos + d + 1))]:
                for j in r:
                    if arr[pos] > arr[j]:
                        dp[pos] = max(dp[pos], dp[j] + 1)
                    else:
                        break
        # print([[num, jumps] for num, jumps in zip(arr, dp)])
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxJumps(arr=[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], d=2) == 4)
    print(solution.maxJumps(arr=[3, 3, 3, 3, 3], d=3) == 1)
    print(solution.maxJumps(arr=[7, 6, 5, 4, 3, 2, 1], d=1) == 7)
    print(solution.maxJumps(arr=[7, 1, 7, 1, 7, 1], d=2) == 2)
    print(solution.maxJumps(arr=[66], d=1) == 1)
    print(solution.maxJumps(arr=[22, 29, 52, 97, 29, 75, 78, 2, 92, 70, 90, 12, 43, 17, 97, 18, 58, 100, 41, 32],
                            d=17) == 6)
    print(solution.maxJumps(
        arr=[59, 8, 74, 27, 92, 36, 95, 78, 73, 54, 75, 37, 42, 15, 59, 84, 66, 25, 35, 61, 97, 16, 6, 52, 49, 18, 22,
             70, 5, 59, 92, 85], d=20) == 8)

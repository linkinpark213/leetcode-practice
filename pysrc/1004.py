from typing import List


class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        left, right = 0, K
        maxWindow = K
        zeroCount = K - sum(A[left: right])
        while right < len(A):
            if A[right] == 0:
                zeroCount += 1
            while zeroCount > K:
                if A[left] == 0:
                    zeroCount -= 1
                left += 1
            maxWindow = max(right - left + 1, maxWindow)
            right += 1
        return maxWindow


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(solution.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
    print(solution.longestOnes([0, 0, 0, 1], 4))

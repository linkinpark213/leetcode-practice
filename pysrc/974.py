from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefixes = {0: 1}
        ans, count = 0, 0
        for i in range(len(A)):
            key = (count + A[i]) % K
            count += A[i]
            if key in prefixes:
                ans += prefixes[key]
                prefixes[key] += 1
            else:
                prefixes[key] = 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.subarraysDivByK(A=[4, 5, 0, -2, -3, 1], K=5))
    print(solution.subarraysDivByK(A=[5], K=9))

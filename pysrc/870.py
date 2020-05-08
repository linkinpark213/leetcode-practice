from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = sorted(A)
        indsB = [[B[i], i] for i in range(len(B))]
        indsB.sort(key=lambda x: x[0], reverse=True)
        ans = [0] * len(A)
        for num, ind in indsB:
            if num >= A[-1]:
                ans[ind] = A.pop(0)
            else:
                ans[ind] = A.pop()
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))
    print(solution.advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))

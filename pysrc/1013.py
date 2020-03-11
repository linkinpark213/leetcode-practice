from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        left = 0
        right = len(A) - 1
        sumLeft = A[left]
        sumRight = A[right]
        while left < right - 1 and (sumLeft != total // 3 or sumRight != total // 3):
            if sumLeft != total // 3:
                left += 1
                sumLeft += A[left]
            if sumRight != total // 3:
                right -= 1
                sumRight += A[right]
        if left < right - 1 and sumLeft == sumRight and sumLeft == total // 3:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]) == True)
    print(solution.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]) == False)
    print(solution.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]) == True)
    print(solution.canThreePartsEqualSum([18, 12, -18, 18, -19, -1, 10, 10]) == True)
    print(solution.canThreePartsEqualSum([6, 1, 1, 13, -1, 0, -10, 20]) == False)
    print(solution.canThreePartsEqualSum([14, 24, -14, -20, -3, 14, 27, -15, 1, 14]) == True)
    print(solution.canThreePartsEqualSum([1, -1, 1, -1]) == False)

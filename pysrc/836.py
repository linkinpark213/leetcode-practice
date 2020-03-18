from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] >= rec2[2] or rec1[2] <= rec2[0]:
            return False
        if rec1[1] >= rec2[3] or rec1[3] <= rec2[1]:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3]))
    print(solution.isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1]))

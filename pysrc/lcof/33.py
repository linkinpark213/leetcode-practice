from typing import List


class Solution:
    def verifyPostorderInRange(self, postorder: List[int], l: int, r: int) -> bool:
        if l >= r - 1:
            return True
        rootVal = postorder[r - 1]
        mid = r - 1
        while mid >= l and postorder[mid] >= rootVal:
            mid -= 1
        for i in range(l, mid):
            if postorder[i] >= rootVal:
                return False
        return self.verifyPostorderInRange(postorder, l, mid + 1) and self.verifyPostorderInRange(postorder, mid + 1,
                                                                                                  r - 1)

    def verifyPostorder(self, postorder: List[int]) -> bool:
        return self.verifyPostorderInRange(postorder, 0, len(postorder))


if __name__ == '__main__':
    solution = Solution()
    print(solution.verifyPostorder([1, 6, 3, 2, 5]))
    print(solution.verifyPostorder([1, 3, 2, 6, 5]))

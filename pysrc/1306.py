from typing import List


class Solution:
    def backtrack(self, arr: List[int], path: List[int], pos: int) -> bool:
        if arr[pos] == 0:
            return True
        if pos - arr[pos] >= 0 and pos - arr[pos] not in path:
            path.append(pos - arr[pos])
            if self.backtrack(arr, path, pos - arr[pos]):
                return True
            path.pop()
        if pos + arr[pos] < len(arr) and pos + arr[pos] not in path:
            path.append(pos + arr[pos])
            if self.backtrack(arr, path, pos + arr[pos]):
                return True
            path.pop()
        return False

    def canReach(self, arr: List[int], start: int) -> bool:
        return self.backtrack(arr, [], start)


if __name__ == '__main__':
    solution = Solution()
    print(solution.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5) == True)
    print(solution.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0) == True)

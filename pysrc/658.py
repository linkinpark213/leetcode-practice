from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= k:
            return arr

        l, r = 0, len(arr)
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                l = mid
                break
            if arr[mid] > x:
                r = mid
            elif arr[mid] < x:
                l = mid + 1

        while abs(arr[l - 1] - x) <= abs(arr[l] - x):
            l -= 1
        print('l = {}, arr[l] = {}'.format(l, arr[l]))
        ans = [arr[l]]
        l, r = l - 1, l + 1
        while len(ans) < k:
            if r >= len(arr) or l >= 0 and abs(arr[l] - x) <= abs(arr[r] - x):
                ans.insert(0, arr[l])
                l -= 1
            else:
                ans.append(arr[r])
                r += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findClosestElements([1, 2, 3, 4, 5], k=4, x=3))
    print(solution.findClosestElements([1, 1, 1, 10, 10, 10], k=1, x=9))
    print(solution.findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], k=3, x=5))

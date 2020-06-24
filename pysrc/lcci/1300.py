from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr = sorted(arr)
        n, curr, minDiff = len(arr), 0, target - arr[0] * len(arr)
        if arr[0] * n >= target:
            return int(0.5 + target / n)
        if sum(arr) <= target:
            return arr[-1]

        ans = arr[0]
        for i, num in enumerate(arr):
            curr += num
            temp = int((target - curr) / (n - i - 1) + 0.49999999) if i < n - 1 else num
            diff = abs(curr + temp * (n - i - 1) - target) if i < n - 1 else abs(curr - target)
            print('i = {}, num = {}, temp = {}, diff = {}'.format(i, num, temp, diff))
            if temp >= num and (i == n - 1 or temp <= arr[i + 1]) and diff < minDiff:
                minDiff = diff
                ans = temp
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findBestValue(arr=[4, 9, 3], target=10))
    print(solution.findBestValue(arr=[2, 3, 5], target=10))
    print(solution.findBestValue(arr=[60864, 25176, 27249, 21296, 20204], target=56803))
    print(solution.findBestValue(arr=[1547, 83230, 57084, 93444, 70879], target=71237))
    print(solution.findBestValue(arr=[1, 2, 23, 24, 34, 36], target=110))

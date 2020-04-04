from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ascending = [(-1, -1)]
        descending = [(-1, -1)]
        for i in range(len(height)):
            if height[i] > ascending[-1][1]:
                ascending.append((i, height[i]))
        ascending.pop(0)

        for i in range(len(height) - 1, -1, -1):
            if height[i] > descending[-1][1]:
                descending.append((i, height[i]))
        descending.pop(0)
        descending.reverse()

        lptr = 0
        rptr = 0
        volume = []
        for i in range(1, len(height) - 1):
            while descending[rptr][0] < i:
                rptr += 1
            while lptr < len(ascending) and ascending[lptr][0] < i:
                lptr += 1
            lptr -= 1
            volume.append(max(0, min(ascending[lptr][1], descending[rptr][1]) - height[i]))
        return sum(volume)


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

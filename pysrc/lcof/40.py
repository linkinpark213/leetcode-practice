from typing import List


class Solution:
    def swap(self, arr: List[int], l: int, r: int):
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp

    def partition(self, arr: List[int], k: int, l: int, r: int) -> List[int]:
        lptr, rptr = l, r
        pivot = arr[lptr]
        while lptr < rptr:
            while lptr < rptr and arr[rptr] >= pivot:
                rptr -= 1
            self.swap(arr, lptr, rptr)
            while lptr < rptr and arr[lptr] <= pivot:
                lptr += 1
            self.swap(arr, lptr, rptr)

        if lptr < k - 1:
            return self.partition(arr, k, lptr + 1, r)
        elif lptr > k:
            return self.partition(arr, k, l, lptr - 1)
        else:
            return arr[:k]

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return self.partition(arr, k, 0, len(arr) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.getLeastNumbers(arr=[3, 2, 1], k=2))
    print(solution.getLeastNumbers(arr=[0, 1, 2, 1], k=1))
    print(solution.getLeastNumbers(arr=[4, 5, 1, 6, 2, 7, 3, 8], k=4))
    print(solution.getLeastNumbers(arr=[0, 0, 1, 2, 4, 2, 2, 3, 1, 4], k=8))

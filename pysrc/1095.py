class MountainArray:
    def __init__(self, array):
        self.array = array
        self.called = 0

    def get(self, index: int) -> int:
        self.called += 1
        if index < 0:
            raise AssertionError()
        return self.array[index]

    def length(self) -> int:
        self.called += 1
        return len(self.array)


class Solution:
    def binaryFindTarget(self, target: int, mountain_arr: 'MountainArray', l: int, r: int, rising: bool) -> int:
        mid = (l + r) // 2
        vM = mountain_arr.get(mid)
        if l >= r and vM != target:
            return -1
        if vM == target:
            return mid
        elif (vM < target) ^ rising:
            return self.binaryFindTarget(target, mountain_arr, l, mid, rising)
        else:
            return self.binaryFindTarget(target, mountain_arr, mid + 1, r, rising)

    def binaryFindPeak(self, mountain_arr: 'MountainArray') -> int:
        l, r = 0, mountain_arr.length() - 1
        while l < r:
            mid = (l + r) // 2
            vM = mountain_arr.get(mid)
            vL, vR = mountain_arr.get(mid - 1), mountain_arr.get(mid + 1)
            if vM > vL and vM > vR:
                return mid
            if vM < vL:
                r = mid
            elif vM < vR:
                l = mid
        return -1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.binaryFindPeak(mountain_arr)
        vPeak = mountain_arr.get(peak)
        if vPeak == target:
            return peak
        elif vPeak < target:
            return -1
        else:
            index = self.binaryFindTarget(target, mountain_arr, 0, peak - 1, True)
            if index == -1:
                index = self.binaryFindTarget(target, mountain_arr, peak + 1, mountain_arr.length() - 1, False)
            return index


if __name__ == '__main__':
    solution = Solution()
    print(solution.findInMountainArray(mountain_arr=MountainArray(array=[1, 2, 3, 4, 5, 3, 1]), target=3))
    print(solution.findInMountainArray(mountain_arr=MountainArray(array=[0, 1, 2, 4, 2, 1]), target=3))
    print(solution.findInMountainArray(mountain_arr=MountainArray(array=[1, 5, 2]), target=0))
    print(solution.findInMountainArray(mountain_arr=MountainArray(array=[1, 2, 5, 1]), target=0))
    print(solution.findInMountainArray(mountain_arr=MountainArray(array=[0, 1, 2, 4, 2, 1]), target=3))

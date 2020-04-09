from typing import List


class Solution:
    def splitArray(self, A: List[int]) -> bool:
        prefixes = []
        current = 0
        for num in A:
            current += num
            prefixes.append(current)

        N = len(A)
        for j in range(3, N - 3):
            possibleSums = set()
            for i in range(1, j - 1):
                if prefixes[i - 1] == prefixes[j - 1] - prefixes[i]:
                    possibleSums.add(prefixes[i - 1])
            for k in range(j + 2, N - 1):
                if prefixes[k - 1] - prefixes[j] == prefixes[-1] - prefixes[k] and prefixes[-1] - prefixes[
                    k] in possibleSums:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.splitArray([1, 2, 1, 2, 1, 2, 1]) == True)

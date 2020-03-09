from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) == 0: return nums
        ori_r, ori_c = len(nums), len(nums[0])
        if ori_r * ori_c != r * c:
            return nums

        new_matrix = []
        row = []
        for i in range(r * c):
            row.append(nums[i // ori_c][i % ori_c])
            if (i + 1) % c == 0:
                new_matrix.append(row)
                row = []

        return new_matrix


if __name__ == '__main__':
    solution = Solution()
    print(solution.matrixReshape([[1, 2], [3, 4]], 1, 4))
    print(solution.matrixReshape([[1, 2, 3], [4, 5, 6]], 3, 2))

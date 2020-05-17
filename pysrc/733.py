from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = [(sr, sc)]
        originalColor = image[sr][sc]
        if originalColor != newColor:
            while len(queue) > 0:
                r, c = queue.pop(0)
                image[r][c] = newColor
                for i, j in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if i >= 0 and i < len(image) and j >= 0 and j < len(image[0]) and image[i][j] == originalColor:
                        queue.append((i, j))
        return image


if __name__ == '__main__':
    solution = Solution()
    print(solution.floodFill(image=[[1, 1, 1],
                                    [1, 1, 0],
                                    [1, 0, 1]], sr=1, sc=1, newColor=2))

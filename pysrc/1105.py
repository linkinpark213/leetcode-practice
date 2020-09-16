from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [[[-1] * 2 for _ in range(shelf_width + 1)] for __ in range(n)]
        dp[0][books[0][0]][0] = books[0][1]
        dp[0][books[0][0]][1] = books[0][1]
        for i, (w, h) in enumerate(books):
            if i > 0:
                dp[i][w][0] = h + min([_[0] for _ in dp[i - 1] if _[0] > -1])
                dp[i][w][1] = h
                for j in range(shelf_width - w + 1):
                    if dp[i - 1][j][0] > -1:
                        dp[i][w + j][0] = dp[i - 1][j][0] + max(0, h - dp[i - 1][j][1])
                        dp[i][w + j][1] = max(h, dp[i - 1][j][1])

        return min([totalH for totalH, layerH in dp[-1] if totalH > -1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.minHeightShelves(books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelf_width=4))

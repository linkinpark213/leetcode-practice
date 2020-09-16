class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = (D - B) * (C - A)
        area2 = (H - F) * (G - E)
        intersection = max(0, min(C, G) - max(A, E)) * max(0, min(D, H) - max(B, F))
        return area1 + area2 - intersection


if __name__ == '__main__':
    solution = Solution()
    print(solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))

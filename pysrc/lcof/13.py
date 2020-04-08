class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        queue = [(0, 0)]
        beenTo = set()
        while len(queue) > 0:
            i, j = queue.pop()
            if i >= 0 and i < m and j >= 0 and j < n and (i, j) not in beenTo:
                beenTo.add((i, j))
                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if a % 10 + a // 10 + b % 10 + b // 10 <= k:
                        queue.append((a, b))

        return len(beenTo)


if __name__ == '__main__':
    solution = Solution()
    print(solution.movingCount(m=2, n=3, k=1))
    print(solution.movingCount(m=3, n=1, k=0))

class GuessGame:
    def __init__(self, num: int):
        self.num = num

    def guess(self, num: int) -> int:
        if num == self.num:
            return 0
        elif num > self.num:
            return -1
        else:
            return 1


guessGame = GuessGame(6)


def guess(num: int) -> int:
    return guessGame.guess(num)


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n + 1
        while l < r:
            mid = l + (r - l) // 2
            ans = guess(mid)
            if ans == -1:
                r = mid - 1
            elif ans == 1:
                l = mid + 1
            else:
                return mid
        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.guessNumber(10))

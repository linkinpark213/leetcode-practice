class Solution:
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))

        dayNum = day

        dayNum += sum(self.monthDays[:(month - 1)])
        if month > 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            dayNum += 1

        return dayNum


if __name__ == '__main__':
    solution = Solution()
    print(solution.dayOfYear('2019-01-09') == 9)
    print(solution.dayOfYear('2019-02-10') == 41)
    print(solution.dayOfYear('2019-03-01') == 60)
    print(solution.dayOfYear('2000-03-01') == 61)
    print(solution.dayOfYear('1990-03-25') == 84)

class Solution:
    dayNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dayCount = (year - 1970) * 365 + sum(self.monthDays[:(month - 1)]) + day - 1
        dayCount += sum(1 for i in range(1972, year, 4))
        dayCount += 1 if year % 4 == 0 and month > 2 else 0
        return self.dayNames[(3 + dayCount) % 7]


if __name__ == '__main__':
    solution = Solution()
    print(solution.dayOfTheWeek(1, 1, 1970) == 'Thursday')
    print(solution.dayOfTheWeek(15, 8, 1993) == 'Sunday')
    print(solution.dayOfTheWeek(18, 7, 1999) == 'Sunday')
    print(solution.dayOfTheWeek(31, 8, 2019) == 'Saturday')
    print(solution.dayOfTheWeek(21, 12, 1980) == 'Sunday')

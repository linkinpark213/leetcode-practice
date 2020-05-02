import random


def rand7():
    return random.randint(1, 7)


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a, b = rand7(), rand7()
        while a + (b - 1) * 7 > 40:
            a, b = rand7(), rand7()
        return 1 + (a + (b - 1) * 7) % 10


if __name__ == '__main__':
    solution = Solution()
    ans = [solution.rand10() for i in range(10000)]
    for i in range(1, 11):
        print('{}: {}%'.format(i, ans.count(i) / len(ans) * 100.))

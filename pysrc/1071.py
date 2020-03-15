from typing import List


class KMPSolution:
    @staticmethod
    def getNext(str1: str) -> List[int]:
        next = [0] * len(str1)
        i = 1
        j = 0
        while i < len(str1):
            while j != 0 and str1[i] != str1[j]:
                j = next[j - 1]
            if str1[i] == str1[j]:
                next[i] = j + 1
            i = i + 1
            j = j + 1
        return next

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(max(len(str1), len(str2))):
            if str1[i % len(str1)] != str2[i % len(str2)]:
                return ''

        next1 = self.getNext(str1)
        next2 = self.getNext(str2)

        length = len(next1) - next1[-1]
        repeat1 = len(next1) // length
        repeat2 = len(next2) // length

        return str1[:length * self.gcd(max(repeat1, repeat2), min(repeat1, repeat2))]


class SimpleSolution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        return str1[:self.gcd(max(len(str1), len(str2)), min(len(str1), len(str2)))]


if __name__ == '__main__':
    for solution in [KMPSolution(), SimpleSolution()]:
        print(solution.gcdOfStrings('ABCABC', 'ABC'))
        print(solution.gcdOfStrings('ABABAB', 'ABAB'))
        print(solution.gcdOfStrings('LEET', 'CODE'))
        print(solution.gcdOfStrings("CXTXNCXTXNCXTXNCXTXNCXTXN",
                                    "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN"))
        print(solution.gcdOfStrings("OBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNO",
                                    "OBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNO"))
        print(solution.gcdOfStrings("FFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKST",
                                    "FFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKST"))
        print(solution.gcdOfStrings(
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))
        print(solution.gcdOfStrings('ABCDEF', 'ABC'))

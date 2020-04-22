class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        s1count, index, s2count = 0, 0, 0
        recall = dict()
        while True:
            s1count += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2count, index = s2count + 1, 0
            if s1count == n1:
                return s2count // n2
            if index in recall:
                s1BeforeLoop, s2BeforeLoop = recall[index]
                s1InLoop, s2InLoop = s1count - s1BeforeLoop, s2count - s2BeforeLoop
                break
            else:
                recall[index] = (s1count, s2count)

        ans = s2BeforeLoop + (n1 - s1BeforeLoop) // s1InLoop * s2InLoop
        rest = (n1 - s1BeforeLoop) % s1InLoop
        for i in range(rest):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans += 1
                        index = 0
        return ans // n2


if __name__ == '__main__':
    solution = Solution()
    # print(solution.getMaxRepetitions(s1="acb", n1=4, s2="ab", n2=2))
    print(solution.getMaxRepetitions(s1="abaacdbac", n1=100, s2="adcbd", n2=4))

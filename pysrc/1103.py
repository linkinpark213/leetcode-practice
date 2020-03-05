from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        nthPerson = 1
        while (nthPerson * (nthPerson + 1)) / 2 < candies:
            nthPerson += 1
        nthPerson -= 1

        rounds = 1 + nthPerson // num_people
        remainingPerson = nthPerson % num_people
        remainingCandies = int(candies - (nthPerson * (nthPerson + 1)) / 2)

        distribution = [0] * num_people

        for i in range(num_people):
            if i < remainingPerson:
                distribution[i] = (i + 1) * rounds + num_people * (rounds * (rounds - 1) // 2)
            elif i == remainingPerson:
                distribution[i] = (i + 1) * (rounds - 1) + num_people * ((rounds - 1) * (rounds - 2) // 2) + remainingCandies
            else:
                distribution[i] = (i + 1) * (rounds - 1) + num_people * ((rounds - 1) * (rounds - 2) // 2)

        return distribution


if __name__ == '__main__':
    solution = Solution()
    print(solution.distributeCandies(7, 4))
    print(solution.distributeCandies(10, 3))

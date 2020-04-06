from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        count = 0
        while l <= r:
            count += 1
            if l != r and people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.numRescueBoats(people=[1, 2], limit=3))
    print(solution.numRescueBoats(people=[3, 2, 2, 1], limit=3))
    print(solution.numRescueBoats(people=[3, 5, 3, 4], limit=5))

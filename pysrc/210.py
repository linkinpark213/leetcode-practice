from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = list(range(numCourses))
        links = [set() for _ in range(numCourses)]
        for u, v in prerequisites:
            links[u].add(v)

        ans = []
        while len(courses) > 0:
            anyMin = False
            for u in courses:
                isMin = True
                for v in links[u]:
                    if v not in ans:
                        isMin = False
                if isMin:
                    anyMin = True
                    courses.remove(u)
                    ans.append(u)
            if not anyMin:
                return []
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findOrder(2, [[1, 0]]))
    print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(solution.findOrder(2, [[0, 1], [1, 0]]))

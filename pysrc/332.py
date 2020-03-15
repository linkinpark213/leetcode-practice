from typing import List


class Solution:
    def dfs(self, tickets, flights, route, pos) -> bool:
        flights[route[-1]].remove(pos)
        route.append(pos)

        i = 0
        if pos in flights.keys():
            while i < len(flights[pos]) and not self.dfs(tickets, flights, route, flights[pos][i]):
                i += 1
        if len(route) != len(tickets) + 1:
            route.pop()
            flights[route[-1]].append(pos)
            flights[route[-1]].sort()
            return False
        return True

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = dict()
        for ticket in tickets:
            if ticket[0] not in flights.keys():
                flights[ticket[0]] = []
            flights[ticket[0]].append(ticket[1])

        for departure in flights.keys():
            flights[departure].sort()

        route = ['JFK']
        i = 0
        while not self.dfs(tickets, flights, route, flights['JFK'][i]):
            i += 1

        return route


if __name__ == '__main__':
    solution = Solution()
    print(solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
    print(solution.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))

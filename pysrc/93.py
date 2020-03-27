from typing import List


class Solution:
    def restoreIpAddressesHelper(self, s: str, n: int, begin: int) -> List[str]:
        if begin:
            return []
        ans = []
        section = ''
        for i, c in enumerate(s[begin:]):
            section = section + c
            if len(section) > 3 or int(section) > 255:
                break
            ans += self.restoreIpAddressesHelper(s, n - 1, begin + i + 1)
        return ans

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restoreIpAddressesHelper(s, 4, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.restoreIpAddresses("25525511135"))

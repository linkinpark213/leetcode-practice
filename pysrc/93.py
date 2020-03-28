from typing import List


class Solution:
    def restoreIpAddressesHelper(self, s: str, n: int, begin: int) -> List[str]:
        if n == 0 or begin >= len(s) or begin < len(s) - n * 3:
            return []
        if s[begin] == '0':
            if n > 1:
                return ['0.' + suffix for suffix in self.restoreIpAddressesHelper(s, n - 1, begin + 1)]
            else:
                if begin == len(s) - 1:
                    return ['0']
                else:
                    return []
        if n == 1:
            return [s[begin:]] if begin >= len(s) - 3 and begin < len(s) and int(s[begin:]) <= 255 else []

        ans = []
        section = ''
        for i, c in enumerate(s[begin:]):
            section = section + c
            if len(section) > 3 or int(section) > 255 or i + (n - 1) > len(s):
                break
            suffices = self.restoreIpAddressesHelper(s, n - 1, begin + i + 1)
            if suffices != []:
                ans.extend(section + '.' + suffix for suffix in suffices)

        return ans

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restoreIpAddressesHelper(s, 4, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.restoreIpAddresses("25525511135"))
    print(solution.restoreIpAddresses("0000"))
    print(solution.restoreIpAddresses("010010"))

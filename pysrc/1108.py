class Solution:
    def defangIPaddr(self, address: str) -> str:
        newaddress = ''
        for c in address:
            if c == '.':
                newaddress += '[.]'
            else:
                newaddress += c
        return newaddress


if __name__ == '__main__':
    solution = Solution()
    print(solution.defangIPaddr('255.255.255.0'))

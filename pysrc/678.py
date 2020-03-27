class Solution:
    def checkValidString(self, s: str) -> bool:
        pStars = 0
        nStars = 0
        current = 0
        for c in s:
            if c == '(':
                current += 1
            elif c == ')':
                current -= 1
                if current < 0:
                    current += 1
                    pStars -= 1
                    if pStars < 0:
                        return False
                if current < nStars:
                    nStars = current
            elif c == '*':
                pStars += 1
                nStars += 1
        return current <= nStars


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkValidString('()') == True)
    print(solution.checkValidString('(*)') == True)
    print(solution.checkValidString('(*))') == True)
    print(solution.checkValidString('*)(*') == True)
    print(solution.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*") == False)
    print(solution.checkValidString("(())(())(((()*()()()))()((()()(*()())))(((*)()") == False)

from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if len(S) == 0:
            return ['']
        else:
            ans = []
            suffices = self.letterCasePermutation(S[1:])
            for s in suffices:
                ans.append(S[0] + s)
            if ord(S[0]) >= ord('A') and ord(S[0]) <= ord('Z'):
                for s in suffices:
                    ans.append(S[0].lower() + s)
            elif ord(S[0]) >= ord('a') and ord(S[0]) <= ord('z'):
                for s in suffices:
                    ans.append(S[0].upper() + s)

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCasePermutation(S="a1b2"))
    print(solution.letterCasePermutation(S="3z4"))
    print(solution.letterCasePermutation(S="12345"))

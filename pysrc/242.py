class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i, c in enumerate('abcdefghijklmnopqrstuvwxyz'):
            if s.count(c) != t.count(c):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram('anagram', 'nagaram'))
    print(solution.isAnagram('rat', 'cat'))
    print(solution.isAnagram('aacc', 'ccac'))

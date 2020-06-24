class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        l = []
        while x != 0:
            l.append(x % 10)
            x = x // 10

        while len(l) > 1:
            left, right = l.pop(0), l.pop()
            if left != right:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))

from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cards = {}
        for card in hand:
            if card not in cards.keys():
                cards[card] = 0
            cards[card] += 1

        for card in sorted(cards.keys()):
            if cards[card] == 0:
                continue
            for i in range(1, W):
                if card + i not in cards.keys() or cards[card + i] < cards[card]:
                    return False
                cards[card + i] -= cards[card]
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
    print(solution.isNStraightHand([1, 2, 3, 4, 5], 4))

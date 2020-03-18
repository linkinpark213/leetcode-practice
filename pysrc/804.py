from typing import List


class Solution:
    d = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
         "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
         "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
         "y": "-.--", "z": "--.."}

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        representations = set()
        for word in words:
            representation = ''
            for c in word:
                representation += self.d[c]
            representations.add(representation)
        return len(representations)


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"]))

from typing import List


class Node:
    def __init__(self, frequency, word):
        self.frequency = frequency
        self.word = word

    def __gt__(self, other):
        if self.frequency > other.frequency or (self.frequency == other.frequency and self.word < other.word):
            return True
        return False

    def __lt__(self, other):
        if self.frequency < other.frequency or (self.frequency == other.frequency and self.word > other.word):
            return True
        return False


class MaxHeap:
    def __init__(self):
        self.items = []

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _leftChild(i):
        return i * 2 + 1

    def push(self, node):
        ptr = len(self.items)
        self.items.append(node)
        while ptr > 0 and self.items[self._parent(ptr)] < self.items[ptr]:
            temp = self.items[self._parent(ptr)]
            self.items[self._parent(ptr)] = self.items[ptr]
            self.items[ptr] = temp
            ptr = self._parent(ptr)

    def pop(self):
        if len(self.items) == 0:
            return None
        ret = self.items[0]
        if len(self.items) != 1:
            last = self.items.pop(-1)
            self.items[0] = last
            ptr = 0
            while (self._leftChild(ptr) < len(self.items) and self.items[ptr] < self.items[self._leftChild(ptr)]) or (
                    self._leftChild(ptr) + 1 < len(self.items) and self.items[ptr] < self.items[
                self._leftChild(ptr) + 1]):
                if self._leftChild(ptr) + 1 >= len(self.items) or self.items[self._leftChild(ptr)] > self.items[
                    self._leftChild(ptr) + 1]:
                    temp = self.items[self._leftChild(ptr)]
                    self.items[self._leftChild(ptr)] = self.items[ptr]
                    self.items[ptr] = temp
                    ptr = self._leftChild(ptr)
                else:
                    temp = self.items[self._leftChild(ptr) + 1]
                    self.items[self._leftChild(ptr) + 1] = self.items[ptr]
                    self.items[ptr] = temp
                    ptr = self._leftChild(ptr) + 1
        return ret


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFrequencies = {}
        for word in words:
            if word not in wordFrequencies.keys():
                wordFrequencies[word] = 1
            else:
                wordFrequencies[word] += 1

        heap = MaxHeap()
        for word, frequency in wordFrequencies.items():
            heap.push(Node(frequency, word))

        print(heap.items)

        ans = []
        for i in range(k):
            ans.append(heap.pop().word)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    print(solution.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))

class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.ptr = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.ptr < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.ptr += 1
        return self.nums[self.ptr - 1]


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.buffer = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.buffer is None and self.iterator.hasNext():
            self.buffer = self.iterator.next()
        return self.buffer

    def next(self):
        """
        :rtype: int
        """
        if self.buffer is not None:
            temp = self.buffer
            self.buffer = None
            return temp
        elif self.iterator.hasNext():
            return self.iterator.next()
        else:
            return None

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.buffer is not None or self.iterator.hasNext()


if __name__ == '__main__':
    # Your PeekingIterator object will be instantiated and called as such:
    iter = PeekingIterator(Iterator([1, 2, 3]))
    while iter.hasNext():
        val = iter.peek()  # Get the next element but not advance the iterator.
        print(val)
        print(iter.next())  # Should return the same value as [val].

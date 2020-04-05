class Record:
    def __init__(self, key, value, timestamp):
        self.key = key
        self.value = value
        self.accessed = 1
        self.timestamp = timestamp
        self.pos = -1

    def __lt__(self, other):
        if self.accessed < other.accessed:
            return True
        elif self.accessed > other.accessed:
            return False
        if self.timestamp < other.timestamp:
            return True
        elif self.timestamp > other.timestamp:
            return False

    def __str__(self):
        return '(key = {}, value = {}, accessed = {}, timestamp = {})'.format(self.key, self.value, self.accessed,
                                                                              self.timestamp)


class MinHeap:
    def __init__(self):
        self.list = []

    def _c(self, i):
        return i * 2 + 1

    def _p(self, i):
        return (i - 1) // 2

    def _swap(self, i, j):
        temp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = temp
        self.list[i].pos = i
        self.list[j].pos = j

    def push(self, element):
        element.pos = len(self.list)
        self.list.append(element)
        self.dragUp(len(self.list) - 1)

    def pop(self):
        if len(self.list) == 0:
            return None
        element = self.list[0]
        self.list[0] = self.list[-1]
        self.list[0].pos = 0
        self.list.pop()
        self.dragDown(0)
        return element

    def dragDown(self, i):
        ptr = i
        while self._c(ptr) < len(self.list):
            if self._c(ptr) < len(self.list) - 1 and self.list[self._c(ptr) + 1] < self.list[self._c(ptr)] and \
                    self.list[self._c(ptr) + 1] < self.list[ptr]:
                self._swap(ptr, self._c(ptr) + 1)
                ptr = self._c(ptr) + 1
            elif self.list[self._c(ptr)] < self.list[ptr]:
                self._swap(ptr, self._c(ptr))
                ptr = self._c(ptr)
            else:
                break

    def dragUp(self, i):
        ptr = i
        while ptr > 0 and self.list[ptr] < self.list[self._p(ptr)]:
            self._swap(ptr, self._p(ptr))
            ptr = self._p(ptr)


class LFUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.timestamp = 0
        self.h = MinHeap()

    def get(self, key: int) -> int:
        self.timestamp += 1
        if self.capacity == 0 or key not in self.d.keys():
            print(-1)
            return -1
        element = self.d[key]
        element.accessed += 1
        element.timestamp = self.timestamp
        self.h.dragDown(element.pos)
        print(element.value)
        return element.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        self.timestamp += 1
        if key in self.d.keys():
            element = self.d[key]
            element.accessed += 1
            element.timestamp = self.timestamp
            element.value = value
            self.h.dragDown(element.pos)
        else:
            if len(self.h.list) == self.capacity:
                elementToKill = self.h.pop()
                self.d.pop(elementToKill.key)
            element = Record(key, value, self.timestamp)
            self.d[key] = element
            self.h.push(element)


class Solution:
    def solve(self, commands, params):
        cache = None
        for i, command in enumerate(commands):
            param = params[i]
            if command == 'LFUCache':
                cache = LFUCache(*param)
            elif command == 'put':
                cache.put(*param)
            elif command == 'get':
                cache.get(*param)


if __name__ == '__main__':
    solution = Solution()
    solution.solve(
        ["LFUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
         "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
         "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
         "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
         "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
         "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
         "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"],
        [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
         [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11],
         [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5],
         [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22],
         [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29],
         [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27],
         [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7],
         [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
    )

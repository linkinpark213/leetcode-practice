class HashListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.memory = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.memory.keys():
            node = self.memory[key]
            if node != self.head:
                if node.prev is not None:
                    node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                if self.tail == node:
                    self.tail = node.prev if node.prev is not None else node
                if node != self.head:
                    node.next = self.head
                    self.head.prev = node
                    self.head = node
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.memory.keys():
            node = self.memory[key]
            node.value = value
            if node != self.head:
                if node.prev is not None:
                    node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                if self.tail == node:
                    self.tail = node.prev if node.prev is not None else node
                if node != self.head:
                    node.next = self.head
                    self.head.prev = node
                    self.head = node
        else:
            if len(self.memory) == 0:
                self.head = HashListNode(key, value)
                self.tail = self.head
                self.memory[key] = self.head
            else:
                node = HashListNode(key, value)
                node.next = self.head
                self.head.prev = node
                self.head = node
                self.memory[key] = node
                if len(self.memory) > self.capacity:
                    node = self.tail
                    self.memory.pop(node.key)
                    self.tail = node.prev
                    node.prev = None
                    self.tail.next = None
                    del node

    def print(self):
        print('MEMORY:')
        for k, v in self.memory.items():
            print('{} => {}'.format(k, v.value))
        print('PRIORITY:')
        ptr = self.head
        while ptr is not None:
            print('({} => {}) - '.format(ptr.key, ptr.value), end='')
            ptr = ptr.next
        print()


if __name__ == '__main__':
    # Your LRUCache object will be instantiated and called as such:
    # cache = LRUCache(2)
    # cache.put(1, 1)
    # cache.print()
    # cache.put(2, 2)
    # cache.print()
    # cache.get(1)
    # cache.print()
    # cache.put(3, 3)
    # cache.print()
    # cache.get(2)
    # cache.print()
    # cache.put(4, 4)
    # cache.print()
    # cache.get(1)
    # cache.print()
    # cache.get(3)
    # cache.print()
    # cache.get(4)
    # cache.print()
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.print()
    cache.put(3, 2)
    cache.print()
    cache.get(3)
    cache.print()
    cache.get(2)
    cache.print()
    cache.put(4, 3)
    cache.print()
    cache.get(2)
    cache.print()
    cache.get(3)
    cache.print()
    cache.get(4)
    cache.print()

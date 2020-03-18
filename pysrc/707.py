class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.tail = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        ptr = self.head
        for i in range(index + 1):
            if ptr is None:
                return -1
            ptr = ptr.next
        return ptr.val if ptr is not None else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = self.head.next
        self.head.next = ListNode(val)
        self.head.next.next = temp
        if temp is None:
            self.tail = self.head.next

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        ptr = self.head
        for i in range(index):
            if ptr is None:
                return
            ptr = ptr.next
        temp = ptr.next
        ptr.next = ListNode(val)
        ptr.next.next = temp
        if temp is None:
            self.tail = ptr.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        ptr = self.head
        for i in range(index):
            if ptr is None:
                return
            ptr = ptr.next
        if ptr.next is None:
            return
        if ptr.next.next is None:
            self.tail = ptr
            self.tail.next = None
        else:
            ptr.next = ptr.next.next

    def __str__(self):
        s = 'MyLinkedList('
        ptr = self.head
        while ptr is not None:
            s += str(ptr.val) + ', '
            ptr = ptr.next
        s += ')'
        return s


if __name__ == '__main__':
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
    print(obj.get(1))
    print(obj)
    obj.addAtHead(1)
    print(obj)
    print(obj.get(1))
    print(obj)
    obj.addAtTail(3)
    print(obj)
    obj.addAtIndex(1, 5)
    print(obj)
    obj.deleteAtIndex(2)
    print(obj)

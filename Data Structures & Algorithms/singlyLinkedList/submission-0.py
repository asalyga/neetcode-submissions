class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def get(self, index: int) -> int:
        if not self.head or index < 0:
            return -1
        i = 0
        node = self.head
        while i != index:
            if not node.next_node:
                return -1
            node = node.next_node
            i += 1
        return node.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val=val, next_node=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val=val, next_node=None)
        if not self.tail:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        if index < 0 or self.head is None:
            return False

        if index == 0:
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
            return True

        prev = self.head
        for _ in range(index - 1):
            if prev.next_node is None:
                return False
            prev = prev.next_node

        target = prev.next_node
        if target is None:
            return False

        prev.next_node = target.next_node
        if target is self.tail:
            self.tail = prev
        return True

    def getValues(self) -> list[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next_node
        return values

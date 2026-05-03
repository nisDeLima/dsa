class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class FirstUnique:
    def __init__(self, nums: list[int]):
        self.seen_twice = set()
        self.val_to_node = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        first = self.head.next
        return first.val if first is not self.tail else -1

    def add(self, value: int) -> None:
        if value in self.seen_twice:
            return

        if value in self.val_to_node:
            self._remove(self.val_to_node.pop(value))
            self.seen_twice.add(value)
        else:
            self._insert_before_tail(Node(value))
            self.val_to_node[value] = self.tail.prev

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_before_tail(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

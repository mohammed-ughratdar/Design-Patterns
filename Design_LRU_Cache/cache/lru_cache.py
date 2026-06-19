from models.node import Node
from threading import Lock

class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")

        self.capacity = capacity
        self.cache : {int: Node} = {}
        self.size = 0

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.lock = Lock()

    def get(self, key: int) -> int:
        with self.lock:
            node = self.cache.get(key)

            if not node:
                return -1

            self._move_to_head(node)
            return node.value

    def _move_to_head(self, node: Node):
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def put(self, key: int, value: int):
        with self.lock:
            node = self.cache.get(key)

            if node:
                node.value = value
                self._move_to_head(node)
                return

            new_node = Node(key, value)
            if self.size >= self.capacity:
                lru_node = self._remove_tail()
                del self.cache[lru_node.key]
                self.size -= 1

            self._add_to_head(new_node)
            self.cache[key] = new_node
            self.size += 1

    def _remove_tail(self) -> Node:
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node
            


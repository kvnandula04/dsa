class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key: Node
        self.size = 0

        # Dummy head and tail nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def add_node(self, node):
        # Always add the new node right after head
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def move_node_to_front(self, node):
        self.remove_node(node)
        self.add_node(node)

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        # Move the accessed node to the front (most recently used)
        self.move_node_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value of the existing node and move it to the front
            node = self.cache[key]
            node.value = value
            self.move_node_to_front(node)
        else:
            # Create a new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_node(new_node)
            self.size += 1

            if self.size > self.capacity:
                # Evict the least recently used node (node before tail)
                lru_node = self.tail.prev
                self.remove_node(lru_node)
                del self.cache[lru_node.key]
                self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

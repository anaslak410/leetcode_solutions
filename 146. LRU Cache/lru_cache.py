class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapa = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:

        item = self.mapa.get(key)

        if item is None:
            return -1

        elif self.head.key == key:
            return item.val

        elif self.tail.key == key:
            nekst = self.tail.nekst
            nekst.prev = None
            self.tail = nekst

        else:
            prev = item.prev
            nekst = item.nekst
            prev.nekst = nekst
            nekst.prev = prev

        item.nekst = None
        item.prev = self.head
        self.head.nekst = item
        self.head = item

        return item.val

    def put(self, key: int, value: int) -> None:
        mapa = self.mapa
        item = mapa.get(key)
        if item is not None:
            item.val = value
            self.get(key)
        elif self.tail is None:
            node = Node(None, None, value, key)
            self.head = node
            self.tail = node
            mapa[key] = node
            self.capacity = self.capacity - 1
        elif self.capacity > 0:
            node = Node(None, self.head, value, key)
            self.head.nekst = node
            self.head = node
            mapa[key] = node
            self.capacity = self.capacity - 1
        else:
            node = Node(None, self.head, value, key)
            self.head.nekst = node
            self.head = node

            del_key = self.tail.key
            self.tail = self.tail.nekst
            self.tail.prev = None

            mapa[key] = node
            mapa.pop(del_key)


class Node:
    def __init__(self, nekst=None, prev=None, val=0, key=0):
        self.key = key
        self.val = val
        self.nekst = nekst
        self.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

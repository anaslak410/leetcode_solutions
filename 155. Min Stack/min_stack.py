

class MinStack:

    def __init__(self):
        self._items = []

    def push(self, val: int) -> None:
        if ((not self._items) or (val < self.getMin())):
            item = Item(val, val)
            self._items.append(item)
        else:
            item = Item(val, self.getMin())
            self._items.append(item)

    def pop(self) -> None:
        self._items.pop()

    def top(self) -> int:
        return self._items[-1].value

    def getMin(self) -> int:
        return self._items[-1].mina


class Item:
    def __init__(self, value, mina):
        self.value = value
        self.mina = mina


if __name__ == "__main__":
    obj = MinStack()
    # print()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    # param_3 = obj.top()
    # print(param_3)
    # param_4 = obj.getMin()

class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0 for n in range(self.capacity)]

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n
        return None

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1
        return None

    def popback(self) -> int:
        self.length -= 1
        return self.array[self.length]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [0 for n in range(self.capacity)]
        for idx in range(len(self.array)):
            new_arr[idx] = self.array[idx]
        self.array = new_arr
        return None

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity

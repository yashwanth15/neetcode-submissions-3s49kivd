class DynamicArray:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.arr = [0] * capacity   # fixed-size backing array

    def get(self, i: int) -> int:
        return self.arr[i]          # i is valid per problem

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n             # i is valid per problem

    def pushback(self, n: int) -> None:
        if self.size == self.cap:   # full
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
        new_cap = self.cap * 2
        new_arr = [0] * new_cap
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.cap = new_cap

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap
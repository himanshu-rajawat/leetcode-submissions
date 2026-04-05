class MyHashSet:

    def __init__(self):
        self.data = ["-" for i in range(100000)]

    def add(self, key: int) -> None:
        self.data[key] = key

    def remove(self, key: int) -> None:
        self.data[key] = "-"

    def contains(self, key: int) -> bool:
        if self.data[key]=="-":
            return False
        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
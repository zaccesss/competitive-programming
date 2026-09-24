class MyHashMap:

    def __init__(self):
        # create an array large enough to store all possible keys
        # initialise all values to -1 (means "not found")
        self.map = [-1] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        # store the value at index = key
        self.map[key] = value

    def get(self, key: int) -> int:
        # return the value at index = key
        # if not set, it will be -1
        return self.map[key]

    def remove(self, key: int) -> None:
        # reset the value at index = key back to -1
        self.map[key] = -1

# your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
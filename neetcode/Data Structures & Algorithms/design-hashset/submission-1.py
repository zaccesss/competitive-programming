class MyHashSet:

    def __init__(self):
        # number of buckets to reduce collisions
        self.size = 1000
        
        # create a list of empty buckets (each bucket is a list)
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        # hash function: maps a key to a bucket index
        return key % self.size

    def add(self, key: int) -> None:
        # find the correct bucket for this key
        bucket = self.buckets[self._hash(key)]
        
        # add key only if it is not already present
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        # find the correct bucket for this key
        bucket = self.buckets[self._hash(key)]
        
        # remove key if it exists in the bucket
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        # check if key exists in its corresponding bucket
        return key in self.buckets[self._hash(key)]


# your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
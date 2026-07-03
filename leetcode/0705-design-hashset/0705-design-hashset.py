class MyHashSet:

    def __init__(self):
        # Number of buckets to reduce collisions
        self.size = 1000
        
        # Create a list of empty buckets (each bucket is a list)
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Hash function: maps a key to a bucket index
        return key % self.size

    def add(self, key: int) -> None:
        # Find the correct bucket for this key
        bucket = self.buckets[self._hash(key)]
        
        # Add key only if it is not already present
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        # Find the correct bucket for this key
        bucket = self.buckets[self._hash(key)]
        
        # Remove key if it exists in the bucket
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        # Check if key exists in its corresponding bucket
        return key in self.buckets[self._hash(key)]
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        # Used k to store kth position.
        self.k = k

        # Used min heap to store top k elements.
        self.heap = nums

        heapq.heapify(self.heap)

        # Removed extra elements.
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        # Added new value.
        heapq.heappush(self.heap, val)

        # Removed smallest if heap exceeded k.
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Returned kth largest element.
        return self.heap[0]
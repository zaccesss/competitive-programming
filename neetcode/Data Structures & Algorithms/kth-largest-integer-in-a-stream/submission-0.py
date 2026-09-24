import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        # used k to store kth position.
        self.k = k

        # used min heap to store top k elements.
        self.heap = nums

        heapq.heapify(self.heap)

        # removed extra elements.
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        # added new value.
        heapq.heappush(self.heap, val)

        # removed smallest if heap exceeded k.
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # returned kth largest element.
        return self.heap[0]
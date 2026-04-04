from collections import deque

# Why are we using heap, when we can restrict the length of our normal array upto k.
# Answer: The complexity of add() using simple array will be O(k), if we use the heap, it takes O(log(k)) to insert. Since heap guarantees the smallest element, not all sorted.

# 
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap);
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val);
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


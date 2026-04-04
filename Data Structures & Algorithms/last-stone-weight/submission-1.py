class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)
        while(len(max_heap) > 1):
            max1 = -1 * heapq.heappop(max_heap);
            max2 = -1 * heapq.heappop(max_heap);
            if(max1 < max2):
                heapq.heappush(max_heap, -1*(max2-max1))
            elif(max1 > max2):
                heapq.heappush(max_heap, -1*(max1-max2))
        return (heapq.heappop(max_heap) * -1) if len(max_heap) > 0 else  0
# # Intuitive O(N^2))
# While array has element more than 1:
#     take the 2 max O(n)
#     do collision, update weight


# # Optimized O(N Log(n))
# While array has element more than 1:
#     take max from maxHeap
#     do collision, update weight
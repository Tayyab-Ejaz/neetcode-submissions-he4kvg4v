class Solution:
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     minHeap = []
    #     for x, y in points:
    #         dis = x**2 + y**2
    #         minHeap.append([dis, x, y])
        
    #     heapq.heapify(minHeap)

    #     res = []
    #     while k > 0:
    #         point = heapq.heappop(minHeap)
    #         res.append(point[1:])
    #         k -= 1

    #     return res
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dis = -(x**2 + y**2)
            maxHeap.append([dis, x, y])
            heapq.heapify(maxHeap)
            if(len(maxHeap) > k):
                heapq.heappop(maxHeap)
        
        res = [x[1:] for x in maxHeap]
        
        return res
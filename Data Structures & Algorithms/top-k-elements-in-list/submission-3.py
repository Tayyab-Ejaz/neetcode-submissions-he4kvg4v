class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        queue = []
        for key, frequency in c.items():
            heapq.heappush(queue, [frequency, key])
            if(len(queue) > k):
                heapq.heappop(queue)
        return [item[1] for item in queue];      
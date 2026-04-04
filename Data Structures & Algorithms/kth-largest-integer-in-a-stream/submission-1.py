class KthLargest:
    nums = []
    k = None
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(list(nums))
        self.k = k

    def add(self, val: int) -> int:
        i = 0
        while(i < len(self.nums) and self.nums[i] < val):
            i += 1
        self.nums.insert(i, val)
        return self.nums[len(self.nums) - self.k]

# [1,2,3,3,3,5,6,7,8]
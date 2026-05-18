class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        i, j = 0, len(height) - 1

        leftMax, rightMax = 0, 0
        
        while(i < j):
            if(height[i] < height[j]):
                if(height[i] < leftMax):
                    total += leftMax - height[i]
                else: 
                    leftMax = height[i]
                i += 1
            else:
                if(height[j] < rightMax):
                    total += rightMax - height[j]
                else:
                    rightMax = height[j]
                j-=1
        return total
        
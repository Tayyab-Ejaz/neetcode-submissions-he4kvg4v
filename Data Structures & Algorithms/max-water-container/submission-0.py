class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        i,j = 0, len(heights) - 1
        while(i < j):
            area = (j - i) * min(heights[j], heights[i])
            if(area > max_area):
                max_area = area;
            
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
        return max_area

        


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        i = 0
        j = len(heights) - 1

        while i < j:
            area = (j - i) * min(heights[j],heights[i])
            if area > res:
                res = area 
            if heights[j] > heights[i]:
                i += 1
            elif heights[j] <= heights[i]:
                j -= 1
        return res
            
            

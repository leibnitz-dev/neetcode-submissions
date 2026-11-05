class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) time and space.
        if not height:
            return 0
        n = len(height)

        lmax = [0]*n 
        cmx = 0
        for i in range(n):
           lmax[i] = cmx 
           cmx = max(cmx, height[i])
        
        rmax = [0]*n
        cmx = 0 
        for i in range(n-1, -1, -1):
            rmax[i] = cmx
            cmx = max(cmx, height[i])
        
        wt = 0
        for i in range(n):
            w = min(lmax[i], rmax[i]) - height[i]
            if w > 0:
                wt += w
        
        return wt 



class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        res=maxL=maxR=0
        while i<j:
            maxL=max(maxL,height[i])
            maxR=max(maxR,height[j])
            if height[i]<height[j]:
                res+=maxL-height[i]
                i+=1
            else:
                res+=maxR-height[j]
                j-=1
        return res
      

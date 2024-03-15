
import collections
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)
        
        res = 0
        
        res = collections.Counter(nums1) & collections.Counter(nums2)
        
        if len(res):
            return min(res.keys())
        return -1


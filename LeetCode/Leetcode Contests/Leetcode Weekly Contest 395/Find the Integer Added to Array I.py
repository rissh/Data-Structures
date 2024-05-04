
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        
        res = 0
        n = len(nums1)
        
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        
        res = sum2 - sum1
        if res:
            return int(res / n)
        return 0



class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        
        res1, res2 = set(),set()
        
        for num in nums1:
            if num not in s2:
                res1.add(num)

        for num in nums2:
            if num not in s1:
                res2.add(num)
                
                        
        return [list(res1),list(res2)]     
      


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        '''
        result = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                result.append(nums1[i])
                nums2.remove(nums1[i])
         
        return result    
        '''
        
        arr = []
        for i in nums2:
            if i in nums1:

                arr.append(i)
                nums1.remove(i)
                
        return arr
        

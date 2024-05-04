
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)
        nums1.sort()
        nums2.sort()
        res = float('inf')

        for num1 in nums1:
            for num2 in nums2:
                x = num2 - num1
                temp = sorted([num + x for num in nums1])
                i, j, skip = 0, 0, 2
                while i < len(temp) and j < m:
                    if temp[i] == nums2[j]:
                        i += 1
                        j += 1
                    else:
                        i += 1
                        skip -= 1
                        if skip < 0:
                            break
                if j == m and (i - j) <= 2:
                    res = min(res, x)

        return res if res != float('inf') else -1
        

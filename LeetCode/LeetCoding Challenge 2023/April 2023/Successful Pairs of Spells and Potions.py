
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        n = len(spells)
        m = len(potions)

        potions.sort()
        res = []

        for s in spells:
            l,r = 0, m-1
            ind = m

            while l <= r:
                mid = (l + r) // 2
                if s * potions[mid] >= success:
                    r = mid - 1
                    ind = mid
                
                else:
                    l = mid + 1

            res.append(m - ind)

        return res
        


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        n = len(pref)
        arr = [pref[0]]
        curr = pref[0]

        for i in range(1,n):
            arr.append(curr ^ pref[i])
            curr = pref[i]

        return arr
      


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        n = len(arr)
        hashMap = {}

        for i in arr:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1

        target = n // 4
        for key, value in hashMap.items():
            if value > target:
                return key
              

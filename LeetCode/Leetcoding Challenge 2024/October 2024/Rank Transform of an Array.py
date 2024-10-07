
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        n = len(arr)
        hashMap = {}
        nums = sorted(set(arr))
        rank = 1

        for num in nums:
            hashMap[num] = rank
            rank += 1

        for i in range(n):
            arr[i] = hashMap[arr[i]]

        return arr
        

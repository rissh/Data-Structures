
from sortedcontainers import SortedSet

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0] * n
        hashMap = defaultdict(int)
        Set = SortedSet()

        for i in range(n):
            if hashMap[nums[i]] > 0:
                pair = (hashMap[nums[i]], nums[i])
                if pair in Set:
                    Set.remove(pair)

            hashMap[nums[i]] += freq[i]

            if hashMap[nums[i]] > 0:
                Set.add((hashMap[nums[i]], nums[i]))

            if Set:
                max_freq_pair = Set[-1]
                res[i] = max_freq_pair[0]

        return res
      

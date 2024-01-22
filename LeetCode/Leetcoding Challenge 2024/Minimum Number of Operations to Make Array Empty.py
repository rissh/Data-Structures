
from collections import defaultdict

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        hashMap = Counter(nums)
        res = 0

        for n, c in hashMap.items():
            if c == 1:
                return -1
            res += math.ceil(c / 3)

        return res

        '''
        n = len(nums)
        num_frequency = defaultdict(int)
        res = 0

        for num in nums:
            num_frequency[num] += 1
        
        for value, frequency in num_frequency.items():
            while frequency:
                if frequency == 1:
                    return -1  
                if frequency == 4 or frequency == 2:
                    frequency -= 2
                    res += 1
                else:
                    frequency -= 3
                    res += 1
        
        return res

        '''
      

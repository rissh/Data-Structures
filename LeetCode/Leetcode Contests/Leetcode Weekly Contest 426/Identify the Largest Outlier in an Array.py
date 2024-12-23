
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        
        n = len(nums)
        totalSum = sum(nums)
        hashMap = Counter(nums)
        res = float('-inf')
        
        for num in nums:
            remainingSum = totalSum - num

            if remainingSum % 2 == 0:
                p = remainingSum // 2
                hashMap[num] -= 1

                if hashMap[p] > 0:
                    res = max(res, num)

                hashMap[num] += 1
        
        return res
      

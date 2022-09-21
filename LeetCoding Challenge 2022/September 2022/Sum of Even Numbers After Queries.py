
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        se = 0
        ans = []
        for i in nums:
            if(i%2==0):
                se += i
        for i in queries:
            if(nums[i[1]]%2 and i[0]%2):
                se+= nums[i[1]] + i[0]
                nums[i[1]] += i[0]
            elif(nums[i[1]]%2==0 and i[0]%2):
                se -= nums[i[1]]
                nums[i[1]] += i[0]
            elif(nums[i[1]]%2 and i[0]%2==0):
                nums[i[1]] += i[0]
            else:
                se += i[0]
                nums[i[1]] += i[0]
            ans.append(se)
        return ans
      

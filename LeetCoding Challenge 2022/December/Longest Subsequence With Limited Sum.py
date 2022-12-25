
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        maxi = list(accumulate(nums))
        for i in queries:
            for j in range(len(maxi)):
                if maxi[j] > i:
                    ans.append(j)
                    break
                elif j == len(maxi)-1:
                    ans.append(j+1)
        return ans
        

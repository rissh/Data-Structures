
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        s = 0
        sum_map = {}
        for i in nums:
            s+=i 
            s= s%k
            if s in sum_map:
                sum_map[s]+=1
            else:
                sum_map[s] = 1

        for i in sum_map:
            su = sum_map[i]
            if i==0:
                count = count + (su*(su -1))//2 + su
            else:
                count += (su*(su -1))//2
        return count
      

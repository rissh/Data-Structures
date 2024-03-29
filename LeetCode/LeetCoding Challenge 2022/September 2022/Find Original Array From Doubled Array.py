
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        
        c = Counter(changed) 
        
        answer = []
        for num in changed:
            if num in c and c[num] >= 1:
                c[num] -= 1
                if (num * 2) in c and c[(num * 2)] >= 1: 
                    answer.append(num)
                    c[num*2] -= 1 
            
            if len(answer) == len(changed) // 2:
                return answer
        
        return []
      

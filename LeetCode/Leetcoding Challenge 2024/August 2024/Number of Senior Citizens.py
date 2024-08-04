
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        n = len(details)
        count = 0
        
        for detail in details:
            res = int(detail[11:13])
            age = 60
            
            if res > age:
                count += 1
                
        return count
        

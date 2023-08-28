
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        k = 0
        p = 0
        for i in data:
            p = f'{i:08b}'
            if k == 0:
                if(p[:5] == "11111"):
                    return False
                elif(p[:4] == "1111"):
                    k = 3
                elif(p[:3] == "111"):
                    k = 2
                elif(p[:2] == "11"):
                    k = 1
                elif(p[0] == "0"):
                    k = 0
                else:
                    return False
            else:
                if(p[:2] == "10"):
                    k -= 1
                else:
                    return False
        if(k != 0):
            return False
        return True
      

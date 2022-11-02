
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        queue = [(start, 0)]
        seen = {start}
        
        while queue:
            code, n = queue.pop(0)
            if code == end:
                return n
            for j in ['A', 'C', 'G', 'T']:
                for i in range(8):
                    temp = code[:i] + j + code[i+1:]
                    if temp in bank and temp not in seen:
                        queue.append((temp, n+1))
                        seen.add(temp)
        return -1
      

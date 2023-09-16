
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans=[]
        row,prvRow = [],[]
        
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(prvRow[j-1]+prvRow[j])
            prvRow = row
            ans.append(row)
            
        return and


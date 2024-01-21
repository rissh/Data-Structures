
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        res = 0
        prev = 0

        for row in bank:
            curr = row.count("1")
            if curr:
                res += curr * prev
                prev = curr

        return res
        
        '''
        n = len(bank)
        m = len(bank[0])
        res = 0

        prev = bank[0].count("1")

        for i in range(1, n):
            curr = bank[i].count("1")

            if curr:
                res += (prev * curr)
                prev = curr

        return res  

        '''      

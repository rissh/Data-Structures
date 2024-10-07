
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        n = len(skill)
        total = sum(skill)

        if (2 * total) % n:
            return -1

        res = 0
        hashMap = Counter(skill)
        target = (2 * total) // n

        for s in skill:
            if not hashMap[s]:
                continue
            
            hashMap[s] -= 1
            diff = target - s
            if not hashMap[diff]:
                return -1

            res += s * diff
            hashMap[diff] -= 1

        return res


        '''
        n = len(skill)
        res = 0
        skill.sort()
        
        for i in range(n//2):
            if(skill[i] + skill[n-i-1] != skill[0] + skill[n-1]):
                return -1
            res += skill[i]*skill[n-i-1]
            
        return res    
        ''' 


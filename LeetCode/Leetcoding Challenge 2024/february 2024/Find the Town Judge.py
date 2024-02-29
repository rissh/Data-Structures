
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # find all the people who trust and make sure number match
        people_who_trust = set()
        for a,b in trust:
            people_who_trust.add(a)

        if len(people_who_trust) != n-1:
            return -1

        # Find potentail judge
        potentail_judge = None
        for i in range(1,n+1):
            if i not in people_who_trust:
                potentail_judge = i

        # Everybody trust the judge
        people_who_trust_judge = set()
        for a,b in trust:
            if b == potentail_judge:
                people_who_trust_judge.add(a)

        if len(people_who_trust_judge) == n-1:
            return potentail_judge
        return -1
      

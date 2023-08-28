
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        n = len(tasks)
        task = Counter(tasks)

        c=0
        for i in task:
            n=task[i]
            if task[i]==1:
                return -1
            if n%3==0:
                c+=n//3
            else:
                k=n%3
                c+=n//3+1

        return c


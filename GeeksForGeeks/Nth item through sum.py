
#User function Template for python3

class Solution:
    def nthItem(self, L1, L2, A, B, N):
        # code here
        new_list = []
        hashset = set()
        for a in A:
            for b in B:
                if a+b not in hashset:
                    new_list.append(a+b)
                    hashset.add(a+b)
        new_list.sort()
        if N> len(new_list):
            return -1
        else: return new_list[N-1]
        

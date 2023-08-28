
def lcs(s, t) :
	n = len(s)
	m = len(t)
	prev = [0 for i in range(m+1)]
	cur = [0 for i in range(m+1)]
	for ind1 in range(1,n+1):
		for ind2 in range(1,m+1):
			if(s[ind1-1] == t[ind2-1]):
				cur[ind2] = 1 + prev[ind2-1]
			else:
				cur[ind2] = max(prev[ind2],cur[ind2-1])
		prev = [x for x in cur]
	return prev[m]

class Solution:
    def longestPalindromeSubseq(self, nums: str) -> int:
        s = nums
        t = nums[::-1]
        return lcs(s,t)
        

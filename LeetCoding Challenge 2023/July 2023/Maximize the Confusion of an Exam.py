
def largestWindow(s,k):
    low = 0
    countF = 0
    countT = 0
    maxi = 1
    for i in range(len(s)):
        if(s[i] == 'F'):
            countF += 1
        if(s[i] == 'T'):
            countT += 1    
        while(min(countT,countF) > k):
            if(s[low] == 'F'):
                countF -= 1
            if(s[low] == 'T'):
                countT -= 1    
            low += 1
        maxi = max(maxi,i-low+1)
    return maxi   

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return largestWindow(answerKey,k)

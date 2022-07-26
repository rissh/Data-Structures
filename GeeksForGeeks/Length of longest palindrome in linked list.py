
# your task is to complete this function
# function should return an integer
'''
class node:
    def __init__(self):
        self.data = None
        self.next = Non
'''
class Solution:
    def maxPalindrome(self,head):
        # Code here
        l,l2=[],[]
        while(head!=None):
            l.append(head.data)
            head=head.next
        for i in range(0,len(l)):
            for j in range(i,len(l)+1):
                a=list(l[i:j])
                if a==a[::-1] and a!=[] and len(a)>=1:
                    l2.append(len(l[i:j]))
        return max(l2)
      

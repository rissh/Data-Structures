
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ans=[]

        for i in lists:
            x=i
            while x:
                ans+=[x.val]
                x=x.next
        ans=sorted(ans,reverse=True)

        res=None

        for i in ans:
            res=ListNode(i,res)
        return res
        
        

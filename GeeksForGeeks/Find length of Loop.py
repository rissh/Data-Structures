
#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''

#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    #Your code here
    count = 0
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if fast == slow:
            count += 1
            slow = slow.next
           
            while fast != slow:
                count += 1
                slow = slow.next
           
            return count
    return 0
    

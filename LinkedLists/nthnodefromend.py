class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head,n):
    dummy = ListNode(0, head)
    
    left = dummy
    right = head
    
    while n > 0 and right: # this puts a gap of n nodes between left and right
        right = right.next
        n -= 1
        
    while right:
        left = left.next
        right = right.next
        
   
    return left.next
  


    
        
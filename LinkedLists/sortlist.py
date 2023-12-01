"""
we will use Merge sort:
1. Base case: if the length of the linked list is less than or equal to 1,
then the list is already sorted.
2. Split the linked list into two halves. we will use the "slow and fast 
pointer" technique to find the midpoint of the linked list.
3. Recursively sort the left and right halves of the linked list.
4. Merge the two sorted halves of the linked list.

"""

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        
        
def sort_list(head):
    #base case: if the length of the linked list is less than or equal to 1
    if not head or not head.next:
        return head
    
    #split the linked list into halves using slow and fast pointer
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next  #moves 1 step
        fast = fast.next.next #moves 2 steps
    #the midpoint of the linkedlist
    mid = slow.next
    #separate the left and right halves
    slow.next = None
    
    #recursively sort the left and the right halves of the linked list
    left = sort_list(head)
    right = sort_list(mid)
    
    #merge the two sorted halves of the linked list
    dummy = ListNode(0)
    curr = dummy
    
    while left and right:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    #append the remaining nodes of the left or right half to the end
    curr.next = left or right
    
    return dummy.next
    
        
        
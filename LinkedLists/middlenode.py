#use the slow and fast pointer approach(Floyd's)

def middle_node(head):
    
    #base case: if the length of the linked list is less than or equal to 1
    if not head or not head.next:
        return head
    
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next               #moves 1 step
        fast = fast.next.next          #moves 2 steps
        
    #the midpoint of the linkedlist
    mid = slow
    
    return mid

def detect_cycle(head):
    
    if not head:
        return head
    
    fast, slow = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:  #there's a cycle
            break
    else:
        return None
    
    while head != slow:   #find the node where the cycle begins
        head, slow = head.next, slow.next
    return head
    
      
        
def detect_cycle(head):
    
    if not head:
        return head
    
    fast, slow = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:  #there's a cycle
            break
    else: #if loop does not exist
        return None
    
    entry = head
    while entry != slow:   #find the node where the cycle begins
        entry, slow = head.next, slow.next
    
    entry.next = None #removes the loop from the linked list
    
    return head
        
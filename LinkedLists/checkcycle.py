#use the slow and fast(hare and tortoise) pointer approach

def check_cycle(head):
    slow, fast = head, head
    
    while fast and fast.next: #we check for both fast and fast.next since if there's no looop fast or fast.next would be null thus returning false
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast: #if both slow and fast next pointer point to the same node then there's a cycle
            return True
    return False
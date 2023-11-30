 def isPalindrome(head):
        slow, fast, prev = head, head, None
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        prev = slow
        slow = slow.next
        prev.next = None
        
        while slow:
            slow.next = prev
            prev = slow
            slow = slow.next
            
        fast = head
        slow = prev
        
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
            
        return True
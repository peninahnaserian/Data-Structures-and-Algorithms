 """
 1. we get the middle node using fast and slow pointers
 2. Reverse the second half of the list
 3. Check if the first and second halves are similar(palindrome)
 """
 
 def isPalindrome(head):
     #get the middle node
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next, 
        fast = fast.next.next    #slow will be at the middle node
      
    #reverse the second half of the list starting at the middle(slow)  
    prev = None
    
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    
    #check if both halves are similar  
    fast = head
    slow = prev
    
    while slow:
        if fast.val != slow.val: 
            return False
        fast = fast.next, 
        slow = slow.next
        
    return True
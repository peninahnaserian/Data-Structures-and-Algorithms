class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        
        
#Method 1 using recursion T O(n) M O(n)
def reverse(head:ListNode) -> ListNode:
 
        # Base case: If head is empty or has reached the list end
        if head is None or head.next is None:
            return head
 
        # Reverse the rest list
        rest = reverse(head.next)
         
        # Put first element at the end
        head.next.next = head
        head.next = None
 
        # Fix the header pointer
        return rest
    
    
    
head = ListNode(7) 
second = ListNode(8)
third = ListNode(9)
fourth = ListNode(10)
fifth = ListNode(11)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = None


print(reverse(head))

    
#Method 2 using iteration  T O(n) M O(1)
#we use two pointers
def reverse_list(head:ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    prev = None
    curr = head
    
    while curr:
        nxt = curr.nxt
        
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
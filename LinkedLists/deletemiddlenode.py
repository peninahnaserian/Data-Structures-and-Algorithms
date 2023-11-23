# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def delete_middle(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if not head or not head.next:
        return None

    fast, slow = head, head

    while fast and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    prev.next = slow.next

    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
# Create & Handle List operations
class LinkedList:
    def __init__(self):
        self.head = None
 
    # Method to display the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
 
    # Method to add element to list
    def addto_list(self, newdata):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            return
 
        last = self.head
        while last.next:
            last = last.next
 
        last.next = newnode
 
 
# Function to merge the lists
# Takes two lists which are sorted
# joins them to get a single sorted list
def merge_lists(head_a, head_b):
 
    # A dummy node to store the result
    dummy_node = Node(0)
 
    # Tail stores the last node
    tail = dummy_node
    while True:
 
        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if head_a is None:
            tail.next = head_b
            break
        if head_b is None:
            tail.next = head_a
            break
 
        # Compare the data of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
        if head_a.data <= head_b.data:
            tail.next = head_a
            head_a = head_a.next
        else:
            tail.next = head_b
            head_b = head_b.next
 
        # Advance the tail
        tail = tail.next
 
    # Returns the head of the merged list
    return dummy_node.next
 
 
# Create 2 lists
listA = LinkedList()
listB = LinkedList()
 
# Add elements to the list in sorted order
listA.addto_list(5)
listA.addto_list(10)
listA.addto_list(15)
 
listB.addto_list(2)
listB.addto_list(3)
listB.addto_list(20)
 
# Call the merge function
listA.head = merge_lists(listA.head, listB.head)
 
# Display merged list
print("Merged Linked List is:")
listA.print_list()
 

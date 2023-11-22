class Node:
    
    def __init__(self,data):
        self.data = data  #assign data
        self.next = None  #initialize next as null
        
class LinkedList:
    
    def __init__(self):
        self.head = None   #initialize the head
        
    def print_list(self):  #prints contents of linked list starting from head
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    
    def at_beginning(self,newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node
        
    def at_end(self,newdata):
        new_node = Node(newdata)
        
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
    
    def in_between(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        
        new_node = Node(newdata)
        new_node.next = middle_node.next
        middle_node.next = new_node
    
    
    def remove_node(self,remove_key):
        head_val = self.head
        
        if (head_val is not None and head_val.data == remove_key): #it is the first node
            self.head = head_val.next
            head_val = None
            return
        while head_val is not None: #searching for the removekey in the list
            if head_val.data == remove_key:  #found the remove key stop search
                break
            prev = head_val
            head_val = head_val.next
            
        if head_val == None:  #the linked list is empty
            return
        
        prev.next = head_val.next  #change pointer of prev node to be node after removed node
        head_val = None        


#code runner   
if __name__ == '__main__':
    
    llist = LinkedList() 
    
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    llist.head.next = second  #link first node with the second
    
    second.next = third  #link second node with the third node
    
    llist.print_list()
    print("###########")
    
    llist.at_beginning("A")
    llist.print_list()
    print("############")
    
    llist.at_end("Z")
    llist.print_list()
    print("############")

    llist.in_between(second.next,"F")
    llist.print_list()
    print("############")

    llist.remove_node(3)
    llist.print_list()
    print("############")
    
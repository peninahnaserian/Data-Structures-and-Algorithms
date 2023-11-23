#Depth first traversals
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        
root = Node(1)
root.right = Node(3)
root.left = Node(2)

root.left.left = Node(4)
root.left.right = Node(5)


def print_inorder(root):  #left,root,right
    if root:
        #first recur on the left child
        print_inorder(root.left)
        
        #print data of the node
        print(root.val)
        
        #recur on the right child
        print_inorder(root.right)
        

def print_postorder(root):  #left,right,root
 
    if root:
 
        # First recur on left child
        print_postorder(root.left)
 
        # the recur on right child
        print_postorder(root.right)
 
        # now print the data of node
        print(root.val),
 
 

def print_preorder(root):  #root,left,right
 
    if root:
 
        # First print the data of node
        print(root.val),
 
        # Then recur on left child
        print_preorder(root.left)
 
        # Finally recur on right child
        print_preorder(root.right)
        
def print_levelorder(root):
    #base case
    if root is None:
        return
    
    queue = []
    
    queue.append(root)
    
    while(len(queue) > 0):
        print(queue[0].val)
        node = queue.pop(0)
        
        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)
        
print("Preorder traversal of binary tree is")
print_preorder(root)
 
print("\nInorder traversal of binary tree is")
print_inorder(root)
 
print("\nPostorder traversal of binary tree is")
print_postorder(root)

print("\nLevel order traversal of binary tree is")
print_levelorder(root)
#start at the root node
#check if there is a left  node
# check if left is less than root if not print not BST and break
# check if there is a right node
# check if the right node is greater than root of not print not BST and break
# repeat while there is a left or right node
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
def check_binary_search_tree(root:Node):
    
    def valid(node,left,right):
        if not node:
            return True
        if not (node.val < right and node.val > left):
            return False
        return (
                valid(node.left,left,node.val) and 
                valid(node.right, node.val, right)
                )
        
    return valid(root, float("-inf"),float("inf"))



root = Node(8)
root.left = Node(4)
root.right = Node(56)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.left = Node(45)
root.right.right = Node(70)

print(check_binary_search_tree(root))
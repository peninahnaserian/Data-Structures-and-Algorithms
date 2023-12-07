class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

                
 #breadth-first search               
def level_order(root:Node):
    
    if root is None:
        return []
    
    
    queue = [root]
    next_queue = []
    level = []
    result = []
        
    while queue != []:
        for root in queue:
            level.append(root.info)
            if root.left is not None:
                next_queue.append(root.left)
            if root.right is not None:
                next_queue.append(root.right)
            
        result.append(level)
        level = []
        queue = next_queue
        next_queue = []            
    
    return result

#code runner
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(level_order(root))
def leaf_similar(root1, root2):
    
    def find_leaf(root):
        if root.left is None and root.right is None:
            return[root]
        
        if root.left and root.right:
            return find_leaf(root.left) + find_leaf(root.right)
        
        if root.left:
            return find_leaf(root.left)
        
        if root.right:
            return find_leaf(root.right)
        
    return find_leaf(root1) == find_leaf(root2)
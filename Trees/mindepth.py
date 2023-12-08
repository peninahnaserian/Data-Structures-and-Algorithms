def min_depth(root):
    #base case the tree is empty
    if root is None: return 0
    
    #initialize the depth of two subtrees
    left_depth = min_depth(root.left)
    right_depth = min_depth(root.right)
    
    #if both subtrees are empty
    if root.left is None and root.right is None:
        return 1
    #if the left subtree is empty
    if root.left is None:
        return right_depth + 1
    # if the right subtree is empty
    if root.right is None:
        return left_depth + 1
    
    #when the two children functions return its depth
    # pick the minimum out of these two subtrees and return
    return min(left_depth, right_depth) + 1 #adding 1 is the current node which is the parent of the two subtrees...
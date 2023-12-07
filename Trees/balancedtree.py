# height-balanced tree: binary tree in which the height of the left and right subtree of any node differ by not more than one

def is_balanced(root):
    if root is None:
        return True

    # This function will return height/ depth of tree
    def depth(root):
        if root is None:
            return 0
        return max(depth(root.left), depth(root.right)) + 1

    l = depth(root.left)
    r = depth(root.right)

    return (abs(l-r) < 2) and is_balanced(root.left) and is_balanced(root.right)
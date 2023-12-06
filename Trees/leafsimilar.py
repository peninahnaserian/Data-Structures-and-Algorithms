def leaf_similar(root1, root2):
    def find_leaf(root):
        left = []
        right = []
        if root.left == None and root.right == None:
            return [root.val]
        else:
            if root.left != None:
                left = find_leaf(root.left)
            if root.right != None:
                right = find_leaf(root.right)
            return (left + right)

    leaf1 = find_leaf(root1)
    leaf2 = find_leaf(root2)

    return leaf1 == leaf2
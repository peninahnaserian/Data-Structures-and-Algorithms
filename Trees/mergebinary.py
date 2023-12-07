# if two nodes overlap, then sum node values up as the new value of the merged node.
# otherwise, the not null node will be used as the node of the new tree

def merge_trees(root1, root2):

    def construct_tree(root1, root2):
        if not root1 and not root2:
            return None
        if not root2:
            return root1
        if not root1:
            return root2
        
        head = TreeNode(root1.val + root2.val)
        head.left = construct_tree(root1.left, root2.left)
        head.right = construct_tree(root1.right, root2.right)

        return head

    return construct_tree(root1, root2)
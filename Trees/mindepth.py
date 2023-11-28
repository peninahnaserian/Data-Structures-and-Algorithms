def min_depth(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maximum=1e8
        if root==None:
            return 0
        def top_to_bottom(node, depth):
            if not node.left and not node.right:
                self.maximum=min(self.maximum, depth+1)
            if node.left:
                top_to_bottom(node.left, depth+1)
            if node.right:
                top_to_bottom(node.right, depth+1)
        top_to_bottom(root, 0)
        return self.maximum
        
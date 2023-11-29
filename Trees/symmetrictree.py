def is_symmetric(root):
        def is_same(root1, root2):
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
                return False
            left = is_same(root1.left, root2.right)
            right = is_same(root1.right, root2.left)
            return left and right
        
        if not root:
            return True
            
        return is_same(root.left, root.right)
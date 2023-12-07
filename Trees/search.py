  def search(root, val):
         # If the root is None or its value is equal to the target value, return the root
        if not root or root.val == val:
            return root
        
        # If the target value is less than the root's value, search in the left subtree
        if val < root.val:
            return search(root.left, val)
        else:
            # If the target value is greater than the root's value, search in the right subtree
            return search(root.right, val)
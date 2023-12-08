 def maxDepth(root):
        def getDepth(root):
            if root is None:
                return 0
            return max(getDepth(root.left)+1,getDepth(root.right)+1)

        return getDepth(root)        


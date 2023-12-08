def is_same_tree(p, q): #p and q are roots of the two trees
    
    def dfs(node1, node2):

        if node1 is None and node2 is None: #reach at the end of the trees and all matched
            return True

        elif node1 is None or node2 is None: #only one of the two is present
            return False

        elif node1.val != node2.val:  #if the values don't match
            return False

        return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
    
    return dfs(p, q)
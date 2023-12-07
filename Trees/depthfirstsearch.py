#recursive
def walk(root):
    if root is not None:
        print(root)
        walk(root.left)
        walk(root.right)
def preorder(root):
   
    # code here
    return preorder(root.left) + [root.data] + preorder(root.right) if root else []

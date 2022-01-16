def preorder(root):
   
    # code here
    return [root.data]+preorder(root.left)+preorder(root.right) if root else []

 def preorder(self,root):
    return self.preorder(root.left) + [root.data] + self.preorder(root.right) if root else []

#Function to check whether a Binary Tree is BST or not.
def isBST(self, root):
    #code here
    arr = self.preorder(root)

    for i in range(1, len(arr)):
        if arr[i]<=arr[i-1]:
            return False
    return True

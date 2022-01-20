class Solution:
    def __init__(self):
        self.h = 0
    
    #Function to return the diameter of a Binary Tree.
    def calc(self, root, height):
        lh = Solution()
        rh = Solution()
        if root is None:
            height.h = 0
            return 0
        ldia = self.calc(root.left, lh)
        rdia = self.calc(root.right, rh)
        height.h = max(lh.h, rh.h)+1
        return max(lh.h+rh.h+1, max(ldia, rdia))
    
    def diameter(self,root):
        # Code here
        height = Solution()
        return self.calc(root, height)

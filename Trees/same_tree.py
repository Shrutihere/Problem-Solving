class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode], a=0, b=0) -> bool:
        if not p and not q:
            return 1
        if not p or not q or p.val!=q.val:
            return 0
        # print(a,b)
        if not self.isSameTree(p.left, q.left, a+1, b+1) or not self.isSameTree(p.right, q.right, a+1, b+1):
            return 0
        return 1

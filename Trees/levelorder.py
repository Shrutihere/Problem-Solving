    def calc(self,root):
        if not root:
            return 0
        else:
            
            lht = self.calc(root.left)
            rht = self.calc(root.right)
            # print(lht, rht)
            if lht>rht:
                return lht+1
            else:
                return rht+1
    
    def printf(self, root, level):
        if not root:
            return 
        if level==1:
            print(root.data, end=" ")
        else:
            self.printf(root.left, level-1)
            self.printf(root.right, level-1)
    
    def levelOrder(self,root ):
        # Code here
        h = self.calc(root)
        for i in range(1, h+1):
            self.printf(root, i)
        return []

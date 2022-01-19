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

def height(self, root):
    # code here
    return(self.calc(root))

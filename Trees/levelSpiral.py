def height(node):
    if not node:
        return 0
    else:
        lht = height(node.left)
        rht = height(node.right)
        if lht>rht:
            return lht+1
        else:
            return rht+1        
    
def findSpiral(root):
    h = height(root)
    flag = False
    
    for i in range(1, h+1):
        find(root, i, flag)
        flag = not flag
    return []


def find(root, level, flag):
    if not root:
        return
    if level==1:
        print(root.data, end=" ")
    elif level>1:
        if flag:
            find(root.left, level-1, flag)
            find(root.right, level-1, flag)
        else:
            find(root.right, level-1, flag)
            find(root.left, level-1, flag)

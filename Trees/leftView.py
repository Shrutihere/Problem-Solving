def Left(root, level, maxlevel, ans):
    if not root:
        return []
    if maxlevel[0]<level:
        ans.append(root.data)
        maxlevel[0] = level
    Left(root.left, level+1, maxlevel, ans)
    Left(root.right, level+1, maxlevel, ans)
    return ans

def LeftView(root):
    maxlevel = [0]
    return Left(root, 1, maxlevel, [])

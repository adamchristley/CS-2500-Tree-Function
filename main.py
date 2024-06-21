def levels(self):
    if self.root is None:
        return 0
    else:
        leftheight = self.treeHeight(self.root.left)
        rightheight = self.treeHeight(self.root.right)
        return 1 + max(leftheight, rightheight)
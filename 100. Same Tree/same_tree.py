class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True
        self.traverse(p, q)
        return self.result

    def traverse(self, p, q):
        if (p is None) ^ (q is None):
            self.result = False
            return

        if (p is None) and (q is None):
            return

        if p.val != q.val:
            self.result = False
            return

        self.traverse(p.right, q.right)
        self.traverse(p.left, q.left)

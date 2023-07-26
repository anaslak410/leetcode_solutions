class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.isSub = False

        self.traverse(root, subRoot)

        return self.isSub

    def traverse(self, original, subRoot):
        if original is None:
            return
        if self.isSub == True:
            return

        if (self.areSame(original, subRoot)):
            self.isSub = True
            return

        self.traverse(original.left, subRoot)
        self.traverse(original.right, subRoot)

    def areSame(self, first, second):
        if (first is None) and (second is None):
            return True
        if (first is None) ^ (second is None):
            return False
        if (first.val != second.val):
            return False

        left = self.areSame(first.left, second.left)
        if not left:
            return False

        right = self.areSame(first.right, second.right)
        if not right:
            return False

        return True

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        self.traverse(root, 0)

        return self.result

    def traverse(self, root, depth):
        if (root is None):
            return depth

        left = self.traverse(root.left, depth + 1)
        right = self.traverse(root.right, depth + 1)

        if (abs(left - right) > 1):
            self.result = False

        return max(left, right)

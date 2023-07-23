class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.biggest = 0
        self.traverse(root)
        return self.biggest

    def traverse(self, root):
        # print(root)
        if (root is None):
            return 0

        left = self.traverse(root.left)
        right = self.traverse(root.right)

        res = left + right
        if res > self.biggest:
            self.biggest = res

        return max(left + 1, right + 1)

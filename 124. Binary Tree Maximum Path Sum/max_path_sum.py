class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.greatest = root.val
        self.traverse(root)
        return self.greatest

    def traverse(self, head):
        if head is None:
            return 0

        if head.val > self.greatest:
            self.greatest = head.val

        left = self.traverse(head.left)
        right = self.traverse(head.right)

        suma = head.val + left + right

        if suma > self.greatest:
            self.greatest = suma
        if left + head.val > self.greatest:
            self.greatest = left + head.val
        if right + head.val > self.greatest:
            self.greatest = right + head.val

        return max(left + head.val, right + head.val, head.val)

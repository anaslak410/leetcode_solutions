class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.arr = []
        self.traverse(root, 0)
        return self.arr

    def traverse(self, root, depth):
        if root is None:
            return
        if len(self.arr) <= depth:
            self.arr.append([root.val])
        else:
            self.arr[depth].append(root.val)

        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)

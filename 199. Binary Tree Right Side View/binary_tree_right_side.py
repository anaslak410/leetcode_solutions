class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []
        self.traverse(root, 0)

        result = []

        for elem in self.arr:
            result.append(elem[-1])

        return result

    def traverse(self, head, depth):
        if head is None:
            return
        if len(self.arr) - 1 < depth:
            self.arr.append([head.val])
        else:
            self.arr[depth].append(head.val)

        self.traverse(head.left, depth + 1)
        self.traverse(head.right, depth + 1)

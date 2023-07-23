
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.num = 0
        self.traverse(root, float("-inf"))
        return self.num

    def traverse(self, current, biggest):
        if current is None:
            return

        if current.val >= biggest:
            self.num = self.num + 1

        self.traverse(current.left, max(biggest, current.val))
        self.traverse(current.right, max(biggest, current.val))

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        bigger = max(p.val, q.val)
        smaller = min(p.val, q.val)
        current = root

        while True:
            if current.val < smaller:
                current = current.right
            elif current.val > bigger:
                current = current.left
            else:
                return current

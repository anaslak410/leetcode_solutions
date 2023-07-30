class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.construct(preorder, inorder, 0, len(preorder), 0)

    def construct(self, preorder, inorder, start, end, root_start):
        if start >= end:
            return None

        val = None
        index = None

        found = False
        for j in range(root_start, len(preorder)):
            pre_elem = preorder[j]
            for i in range(start, end):
                inord_elem = inorder[i]
                if pre_elem == inord_elem:
                    val = pre_elem
                    index = i
                    root_start = j
                    found = True
                    break
            if found:
                break

        left = self.construct(preorder, inorder, start, index, root_start + 1)
        right = self.construct(
            preorder, inorder, index + 1, end, root_start + 1)

        return TreeNode(val, left, right)

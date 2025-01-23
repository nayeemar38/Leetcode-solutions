class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if there is no root return None
        if not root:
            return None

        # preform swapping using a temporary variable
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # recursively call the function on the left and right child
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return the inverted binary tree
        return root
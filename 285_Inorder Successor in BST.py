# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        if not root or not p:
            return None
        
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        
        return succ
#         self.found = False
#         self.suc = None
#         def dfs(root, p):
#             if not root:
#                 return None
#             dfs(root.left, p)
#             if self.suc:
#                 return
#             if self.found:
#                 self.suc = root
#                 return
#             if root.val == p.val:
#                 self.found = True 
#             dfs(root.right, p)
        
#         dfs(root, p)
#         return self.suc

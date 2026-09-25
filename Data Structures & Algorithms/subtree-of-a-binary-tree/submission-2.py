# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p,q):
            if not p and not q :
                return True
            
            if not p or not q :
                return False
            
            if p.val != q.val:
                return False
            
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        isSameTree(root,subtree)
        return self.isSubtree(root.left,subtree) or self.isSubtree(root.right,subtree)

        
        


        
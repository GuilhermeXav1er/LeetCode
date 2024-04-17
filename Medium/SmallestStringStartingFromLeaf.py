class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        ans=[]

        def dfs(root,ds):
            ds.append(chr(97+root.val))
            if not root.left and not root.right:
                ans.append("".join(ds[:]))
                return
            if root.left:
                dfs(root.left,ds)
                ds.pop()
            if root.right:
                dfs(root.right,ds)
                ds.pop() 

        dfs(root,[])
        ans=sorted([i[::-1] for i in ans])
        return ans[0]

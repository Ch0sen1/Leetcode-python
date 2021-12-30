# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s :
            return 
        stack = []
        curNum = ""
        for c in s:
            if c.isdigit() or c == "-":
                curNum += c
            
            # go to deeper
            elif c == "(" and curNum:
                root = TreeNode(curNum)
                stack.append(root)
                curNum = ""
            
            # back up
            elif c == ")":
                if curNum:
                    node = TreeNode(curNum)
                    parent = stack[-1]
                    curNum = ""
                else:
                    node = stack.pop()
                    parent = stack[-1]
                if parent.left == None:
                    parent.left = node
                else:
                    parent.right = node
        
        if curNum:
            stack =[TreeNode(curNum)]
        
        return stack[0]
                
            
                
        
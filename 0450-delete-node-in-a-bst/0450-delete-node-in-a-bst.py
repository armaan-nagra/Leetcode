# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root
        parent = None
        is_left_child = False

        while curr:
            if curr.val < key:
                parent = curr
                curr = curr.right
                is_left_child = False
            elif curr.val > key:
                parent = curr
                curr = curr.left
                is_left_child = True
            else:
                break
        if curr is None:
            return root
        
        #curr is the node to delete
        
        no_children = (curr.left is None and curr.right is None)
        one_child = (curr.left is None) != (curr.right is None)
        two_children = not no_children and not one_child

        if no_children:
            if parent is None:
                root = None 
            elif is_left_child:
                parent.left = None 
            else:
                parent.right = None 
            
        elif one_child:
            child = curr.left if curr.left else curr.right

            if parent is None:
                root = child 
            elif is_left_child:
                parent.left = child 
            else:
                parent.right = child
        
        else:
            #we're going right to find the left most node in the right subtree
            succ_parent = curr 
            succ = curr.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            
            curr.val = succ.val 

            #remove successor node 
            child = succ.right 
            if succ_parent.left == succ:
                succ_parent.left = child 
            else:
                succ_parent.right = child 

        return root
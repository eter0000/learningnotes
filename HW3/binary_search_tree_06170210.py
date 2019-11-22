#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self,root,val):
        if root.val >= val:
            if root.left is None:
                root.left=TreeNode(val)  #新節點
                return root.left
            else:
                return(Solution().insert(root.left,val))  #再回到insert，root變成root.left
        else:
            if root.right is None:
                root.right=TreeNode(val)
                return root.right
            else:
                return(Solution().insert(root.right,val))  ##再回到insert，root變成root.right
        
    def minnode(self,val):  #找右sub-tree的最小節點
        current_node=val
        while current_node.left!=None:
            current_node=current_node.left 
        return current_node
    
    def maxnode(self,val):  ##找左sub-tree的最大節點
        current_node=val
        while current_node.right!=None:
            current_node=current_node.right
        return current_node
    
    def delete(self,root,target):
        while Solution().search(root,target) is not None: 
            Solution().ddelete(root,target)  #呼叫ddelete
        return root
    
    def ddelete(self,root,target):
        #while Solution().search(root,target) is not None:
        if root is None:
            return root
        elif root.val<target:  #若target大於
            root.right=Solution().ddelete(root.right,target)#往root.right的方向再回到 delete()，此時的root變為root.right
        elif root.val>target:  #若target小於
            root.left=Solution().ddelete(root.left,target)  #往root.left的方向再回到 delete()此時的root變為root.left
        else:    #當target=root.val時
            if root.left is None: # 當左邊為None，右邊可能為None也可能有node
                successor=root.right  # 先把右邊賦予給successor
                root=None  #之後刪除原本root
                return successor
            elif root.right is None:  # 當右邊為None，左邊可能為None也可能有node
                successor=root.left 
                root=None
                return successor
            successor=Solution().maxnode(root.left)  #在successor的左邊找最大值，之後要來填補successor本身的位置
            root.val=successor.val  #將successor的值賦予給root
            root.left=Solution().ddelete(root.left,successor.val) #將root.right裡的sub-tree裡的successor刪除
        return root
    
    def search(self,root,target):
        if root is None: #若是None回傳 None
            return None
        elif root.val==target:
            return root
        elif root.val>=target:
            return Solution().search(root.left,target)
        else:
            return Solution().search(root.right,target)
        
    def modify(self, root, target, new_val):
        if root is None:
            root=TreeNode(new_val)
        else:
            Solution().delete(root,target)
            Solution().insert(root,new_val)
        return root


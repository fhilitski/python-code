import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        trees = list()
        trees.append(root)
        while (len(trees)>0):
            level = trees.pop(0)
            print(level.data)
            right = level.right
            left = level.left
            if (left != None):
                trees.append(left)   
            if (right != None):
                trees.append(right)
			
        return 0
						
		

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

#!/usr/bin/python
# Filename:tree.py
import collections

class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class Tree:
    def __init__(self,node=None):
        self.root=node
    def __preorder__(self,root):
        if root is not None:
            print root.data
            self.__preorder__(root.left)
            self.__preorder__(root.right)
        else:
            pass
    def __inorder__(self,root):
        if root is not None:
            self.__inorder__(root.left)
            print root.data
            self.__inorder__(root.right)
        else:
            pass
    def __postorder__(self,root):
        if root is not None:
            self.__postorder__(root.left)
            self.__postorder__(root.right)
            print root.data
    def preorder(self):
        self.__preorder__(self.root)
    def inorder(self):
        self.__inorder__(self.root)
    def postorder(self):
        self.__postorder__(self.root)
    def preorder2(self):
        stack=[]
        p=self.root
        while p is not None or len(stack)>0:
            if p is not None:
                print p.data
                stack.append(p)
                p=p.left
            else:
                tmp=stack.pop()
                p=tmp.right
    def inorder2(self):
        stack=[]
        p=self.root
        while p is not None or len(stack)>0:
            if p is not None:
                stack.append(p)
                p=p.left
            else:
                tmp=stack.pop()
                print tmp.data
                p=tmp.right
    def levelorder(self):
        if self.root is None:
            return
        queue=collections.deque()
        queue.append(self.root)
        while len(queue)>0:
            tmp=queue.popleft()
            print tmp.data
            if tmp.left is not None:
                queue.append(tmp.left)
            if tmp.right is not None:
                queue.append(tmp.right)
            
        





if __name__=='__main__':
    print "This program is being run by itself"
    #tree=Tree(Node('-',Node('+',Node('a'),Node('*',Node('b'),Node('c'))),Node('/',Node('d'),Node('e'))))
    tree=Tree(None)
    print "preorder:"
    tree.preorder()
    print "inorder:"
    tree.inorder()
    print "postorder:"
    tree.postorder()
    print "preorder2:no recursion:"
    tree.preorder2()
    print "inorder2:no recursion:"
    tree.inorder2()
    print "levelorder:"
    tree.levelorder()

#!/usr/bin/python
# coding:utf-8
# Filename:graph.py

class graph:
    def __init__(self,mydict={}):
        self.mydict=mydict
    def dfs(self,s,li=None):
        if li is None:li=[]
        li.append(s)
        tmp=self.mydict.get(s)
        if tmp is not None:
            for u in tmp:
                if u in li:continue
                self.dfs(u,li)
        return li
    def traverse(self,s):
        S,li=set(),[]
        li.append(s)
        while li:
            u=li.pop()
            if u in S:continue
            S.add(u)
            tmp=self.mydict.get(u)
            if tmp is not None:
                for i in tmp:
                    li.append(i)
            yield u
    def getcircle(self):
        result,no={},0
        stack,li=[],[]
        if len(self.mydict)>0:
            li.append(self.mydict.iterkeys().next())
            while len(li)>0:
                u=li.pop()
                if u in stack:
                    s=stack[stack.index(u):]
                    ss=[s[len(s)-1]]
                    i=len(s)-1
                    while i>=1:
                        for j in range(i-1,-1,-1):
                            if self.mydict.get(s[j]) is not None and s[i] in self.mydict.get(s[j]):
                                i=j
                                ss.append(s[j])
                                break
                    result[no]=ss[::-1]
                    no+=1
                    continue
                stack.append(u)
                tmp=self.mydict.get(u)
                if tmp is not None:
                    for i in tmp:
                        li.append(i)
            return result
        return {}
if __name__ =='__main__':
    #G=graph({0:set([1]),1:set([2]),2:set([3,4]),3:set([0,1])})
    G=graph({0:set([1]),1:set([2]),2:set([3,4]),3:set([0,1])})
    print G.dfs(0)
    print G.dfs(1)
    for i in  G.traverse(0):print i
    print G.getcircle()

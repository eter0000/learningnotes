#!/usr/bin/env python
# coding: utf-8

# In[5]:


#參考網站https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Graphs/breadth-first_search.html
from collections import defaultdict  
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v)
  
    def BFS(self, s): 
        queue=[]
        queue.append(s)
        be_seen=set()  #將還沒被讀到的值放進set
        be_seen.add(s)
        sort=[]
        while len(queue)>=1:
            vertex=queue.pop(0)  #取出第一個值
            vertex_next=self.graph[vertex]  #vertex所連接的點
            for i in vertex_next:
                if i not in be_seen:  #若值還沒被讀到
                    queue.append(i)
                    be_seen.add(i)  
            sort.append(vertex)  
        return sort
    
    def DFS(self, s):
        stack=[]
        stack.append(s)
        be_seen=set()
        be_seen.add(s)
        sort=[]
        while len(stack)>=1:
            vertex=stack.pop()  #取出最後一個值
            vertex_next=self.graph[vertex]
            for i in vertex_next:
                if i not in be_seen:
                    stack.append(i)
                    be_seen.add(i)
            sort.append(vertex)
        return sort


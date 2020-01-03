#!/usr/bin/env python
# coding: utf-8

# In[197]:


#參考網站:http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html
from collections import defaultdict 

class Graph(): 
    def __init__(self, vertices): 
        self.dic = defaultdict(list)
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    
    def addEdge(self,u,v,w): 
        self.dic[w].append([u,v])
    
    def recursive(self, s): 
        for number in range(self.V):
            dist=self.graph[number]  
            for j in range(self.V): #以self.V的長度執行迴圈
                for x in range(self.V):
                    if dist[x]!=0: #該位置值非零時表示有距離
                        con_dist=self.graph[x] #非零值取出放至con_dist
                        for e in range(self.V):
                            if con_dist[e]!=0:  
                                if dist[e]==0: 
                                    dist[e]=con_dist[e]+dist[x] #放入距離值
                                elif dist[e] > con_dist[e]+dist[x]: 
                                    dist[e]=con_dist[e]+dist[x] #更新距離值
            #self.graph[number]=dist 
       
    def Dijkstra(self,s):
        final_dist={}
        self.recursive(s)
        for num in range(self.V):
            self.graph[num][num]=0 #自己和自己的距離為0
            final_dist[str(num)] = self.graph[s][num] #依序放入final_dist
        
        return final_dist
        
    
    ###########################################################################練習用
    def Kruskal(self):
        matrix = [column for column in range(self.V)]
        bingo={}
        dis=sorted(self.dic)
       
        for i in dis:
            for j,s in self.dic[i]:
                if matrix[j]!=matrix[s]:
                    matrix = [matrix[j] if q==matrix[s] else q for q in matrix]
                    bingo[str(j)+'-'+str(s)]=i
                else:
                    pass
        
        return bingo


# In[198]:


g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
           ]


# In[199]:


g.Dijkstra(0)


# In[200]:


g=Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,50)
g.addEdge(2,3,4)


# In[201]:


g.Kruskal()


# In[ ]:





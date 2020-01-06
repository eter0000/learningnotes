#!/usr/bin/env python
# coding: utf-8

# In[1]:


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stacklist = []
        self.len = 0
        

    def push(self, x: int) -> None:
        self.stacklist.append(x)
        self.len+=1

    def pop(self) -> None:
        if self.len == 0:
            pass
        else:
            self.stacklist.pop(self.len-1)
            self.len-=1

    def top(self) -> int:
        return self.stacklist[self.len-1]

    def getMin(self) -> int:
        return min(self.stacklist)


# In[ ]:





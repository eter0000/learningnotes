#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def reverse(self, x: int) -> int:
        if x > 0 and x < 2**31-1:
            a=str(x)
            if int(a[::-1]) > 2**31-1:
                return 0
            else:
                return int(a[::-1])
        else:
            if x < 0 and x > -(2**31-1):
                a=str(x)
                b=a[1:]
                if int('-'+b[::-1]) < -(2**31-1):
                    return 0
                else:
                    return int('-'+b[::-1])
            else:
                return 0


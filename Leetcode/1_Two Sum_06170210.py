#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for t in range(i+1,len(nums)):
                a=nums[i]+nums[t]
                if a==target:
                    return [i,t]


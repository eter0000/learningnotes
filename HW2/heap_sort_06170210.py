#!/usr/bin/env python
# coding: utf-8

# In[75]:


class Solution(object):
    def heap_sort(self,nums):
        if len(nums)<2:
            return nums
        else:
            nums_len=len(nums)
            newlist=[] #先創立一個空的 list 到時候取出的值要放進來
            
            for a in range(nums_len):  #以nums的長度來決定迴圈重複執行的次數
                
                for b in range(nums_len-1,-1,-1): #從最後一個數往前執行迴圈
                    
                    try: #可能會超出index的長度，嘗試執行以下程式碼，若超過index長度則跳到except
                       
                        if 2*b+1 < nums_len: #判斷左邊的子節點
                            
                            if nums[b]<nums[2*b+1]:
                                nums[b],nums[2*b+1]=nums[2*b+1],nums[b] #若nums[b]<nums[2*b+1]則互換位置
    
                        if 2*b+2 < nums_len: #判斷右邊的子節點
                            
                            if nums[b]<nums[2*b+2]:
                                nums[b],nums[2*b+2]=nums[2*b+2],nums[b] #若nums[b]<nums[2*b+2]則互換位置
                    
                    except: #這部分是對錯物值(超出index的長度)的處理動作
                        
                        pass #跳過
                newlist.append(nums.pop(0)) #取出第一個值後刪掉原本的位置(index 0)再 append到空的 newlist
            
            return newlist[::-1] #因為取出值會是由大排到小，因此要從最後一個往前 print


# In[76]:


output=Solution().heap_sort([9,-1,5,2,-6,8,2,1,3,0])
output


# In[ ]:





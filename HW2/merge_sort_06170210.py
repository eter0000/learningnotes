#!/usr/bin/env python
# coding: utf-8

# In[65]:


class Solution(object):
    def merge_sort(self, nums):
        if len(nums)<2:
            return nums
        else:
            middle=int(len(nums)/2) #取 nums長度的一半為切割的點
            
            L=nums[:middle] #L為 nums的前半部
            R=nums[middle:] #R為 nums的後半部
            
            self.merge_sort(L) #因為要繼續切割 list裡面的數，直到長度為 1，所以這邊呼叫自己
            self.merge_sort(R) #同上
           
            l=0 # L的 index
            r=0 # R的 index
            m=0 # nums的 indx
            
            while l<len(L) and r<len(R): #當 L和 R的 index都還沒超過長度時
                
                if L[l]>=R[r]: #若 L的第一個數 >= R的第一個數
                    
                    nums[m]=R[r] #將 R的第一個數放入nums
                    
                    r+=1 #因 R的第一個數已放入 nums，換下一個數和 L比較
                    
                    if r>=len(R): #若 r已 >= R的長度，表示 R裡面的值已跑完
                        
                        nums[m+1:]=L[l:] #將 L剩下的值從 nums的 m+1位置開始放入
                else:
                    
                    nums[m]=L[l] #若 R的第一個數 > L的第一個數，則將 L的地個數放入 nums
                    
                    l+=1 #放入後換下一個數和 R比較
                    
                    if l>=len(L): #若 l已 >= L的長度，表示 L裡的值已跑完
                        
                        nums[m+1:]=R[r:] #將 R剩下的值放入
                
                m+=1 #填完 nums的第一個數後，繼續往下填
        return nums


# In[66]:


output=Solution().merge_sort([0,3,6,1,8,-2,5,-7,-4,0,10,0])
output


# In[ ]:





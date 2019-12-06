#!/usr/bin/env python
# coding: utf-8

# In[10]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def hash1_function(self,key):  #轉換後的值
        from Crypto.Hash import MD5
        new_key=MD5.new()
        new_key.update(key.encode("utf-8"))
        new_hex=new_key.hexdigest()
        new_hex_int=int(str(new_hex),16)
        return new_hex_int
    
    def hash_function(self,key):  #取bucket的位置(餘數)
        from Crypto.Hash import MD5
        new_key=MD5.new()
        new_key.update(key.encode("utf-8"))
        new_hex=new_key.hexdigest()
        new_hex_int=int(str(new_hex),16)
        index=new_hex_int % self.capacity
        return index
    
    def add(self, key):
        index=MyHashSet().hash_function(key)
        hex_int=MyHashSet().hash1_function(key)
        if self.data[index] is None:
            self.data[index]=ListNode(hex_int)
        else:
            l=self.data[index]
            if l.next is None:
                if l.val==hex_int:
                    return
                else:    
                    l.next = ListNode(hex_int)
                    return 
            while l.next is not None:
                l=l.next
                if l.val==hex_int:
                    return
            l.next=ListNode(hex_int)
    
    def remove(self, key):
        index=self.hash_function(key)
        hex_int=self.hash1_function(key)
        k=self.data[index]
        if k is None:
            return 
        
        if k.val==hex_int:
            k=k.next
            self.data[index]=k
        else:
            k=k.next
            if k is None:
                return 
            while k.val != hex_int:
                k=k.next
                if k.next is None:
                    return 
            self.data[index]=k.next
            return
   
    def contains(self, key):
        index=self.hash_function(key)
        if self.data[index] is None:
            return False
        else:
            l=self.data[index]
            hex_int=self.hash1_function(key)
            if l.val==hex_int:
                return True
            else:
                l=l.next
                while l is not None:
                    if l.val==hex_int:
                        return True
                    else:
                        l=l.next
                return False


# In[ ]:





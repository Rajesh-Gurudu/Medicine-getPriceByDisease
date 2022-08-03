#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Medicine:
    def __init__ (self,MedicineName,batch,disease,price):
        self.MedicineName = MedicineName
        self.batch = batch
        self.disease = disease
        self.price = price
        
class Solution:
    @classmethod
    def getPriceByDisease(cls,list_Med,dis):
        result=[]
        for i in list_Med:
            if i.disease.lower() == dis.lower():
                result.append(i.price)
        return result
        
n = int(input())
list_Med = []

for i in range(n):
    MedicineName = input()
    batch = input()
    disease = input()
    price = int(input())
    
    list_Med.append(Medicine(MedicineName,batch,disease,price))
    
dis = input()
answer=Solution.getPriceByDisease(list_Med,dis)

for i in answer:
    print(i)


# In[ ]:





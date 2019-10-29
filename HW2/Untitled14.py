#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
work_dailies = pd.read_excel(r'C:\Users\USER\Desktop\WORK_DAILIES_SORT 的摘要統計量.xlsx')


# In[2]:


work_sleep = pd.read_excel(r'C:\Users\USER\Desktop\WORK_SLEEPS_SORT 的摘要統計量.xlsx')


# In[7]:


left_join = work_dailies.merge(work_sleep, on=['month','date','id'], how='left')
left_join


# In[11]:


left_join.columns.values.tolist()


# In[8]:


file_path = r'./output.xlsx'
writer = pd.ExcelWriter(file_path)
df = pd.DataFrame(left_join)


# In[13]:


df.to_csv(r'./3.csv',columns=['id','month','date','averageStressLevel_Mean','deepSleepDurationInSecond_Mean','lightSleepDurationInSecon_Mean','awakeDurationInSeconds_Mean','activeKilocalories_Mean','bmrKilocalories_Mean','steps_Mean','distanceInMeters_Mean','durationInSeconds_Mean_x','activeTimeInSeconds_Mean', 'floorsClimbed_Mean','minHeartRateInBeatsPerMin_Mean','maxHeartRateInBeatsPerMin_Mean','averageHeartRateInBeatsPe_Mean','restingHeartRateInBeatsPe_Mean'],index=False,sep=',')


# In[ ]:





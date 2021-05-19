#!/usr/bin/env python
# coding: utf-8

#               COLOURS IDENTIFICATION IN IMAGES
#                   ***   TASK #2  ***
#                      @GRIP(MAY-2021)
#                      
#                   THE SPARKS FOUNDATION
# 

# In[1]:



#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


img=cv2.imread(r"C:/Users/Vyas Anjana/Pictures/the bond.jpg")


# In[3]:


plt.figure(figsize=(20,8))
plt.imshow(img)


# In[4]:


rgb1= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[5]:


plt.figure(figsize=(20,8))
plt.imshow(rgb1)


# In[6]:


hsv=cv2.cvtColor(rgb1, cv2.COLOR_RGB2HSV)


# In[7]:


#lower_range = np.array([35,100,100]) #green
#upper_range = np.array([65,255,255])

#lower_range = np.array([15,99,56]) #yellow
#upper_range = np.array([35,255,255])

#lower_range = np.array([0,155,84]) #red
#upper_range = np.array([10,255,255])

#lower_range = np.array([70,50,50]) #sea-green
#upper_range = np.array([95,255,255])

lower_range = np.array([95,50,50]) #blue
upper_range = np.array([130,255,255])


# In[8]:


mask = cv2.inRange(hsv, lower_range, upper_range)


mask = cv2.inRange(hsv, lower_range, upper_range)


# In[9]:



plt.figure(figsize=(20,8))
plt.imshow(mask)


# In[10]:


res = cv2.bitwise_and(rgb1,rgb1,mask=mask)


# In[11]:



plt.figure(figsize=(20,8))
plt.imshow(res)


# In[12]:


cv2.imshow('image',rgb1)


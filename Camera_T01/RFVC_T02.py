#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from skimage import data, io
import matplotlib.pyplot as plt
import matplotlib.image as im
import os
get_ipython().run_line_magic('matplotlib', 'inline')
os.getcwd()
os.chdir('C:/Users/Hector Garcia/Desktop/Camera_T02')
os.getcwd()


# In[10]:


n = 47
image = []
for i in np.arange(n):
    image.append(data.load('C:/Users/Hector Garcia/Desktop/Camera_T02/'+str(i)+'.jpg'))


# In[11]:


#print(len(image))
#print(type(image))
avIm = np.sum(image, axis = 0) / n
aveIm = avIm.astype(np.uint8)
#print(avIm)
#plt.imshow(avIm)


# In[12]:


aveIm = aveIm.astype(np.uint8)
im.imsave("ave.png", aveIm, format = 'png')


# In[13]:


aux = 0
for j in np.arange(n):
    aux += np.square(avIm - image[j])
aux = aux / (n - 1)
stDev = np.sqrt(aux)
print(stDev)


# In[14]:


stDev = stDev.astype(np.uint8)
plt.imshow(stDev)
im.imsave("ImStDev.png", stDev, format = 'png')
#plt.savefig('foo.png')


# In[15]:


print(stDev)


# In[ ]:





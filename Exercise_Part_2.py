#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arcgis


# In[2]:


from arcgis.gis import GIS
gis = GIS()


# In[4]:


map1 = gis.map('Washington, DC')
map1


# In[5]:


import arcpy


# In[6]:


arcpy.analysis.Buffer("voting_sites", "votting_sites_buff", "100 meters")


# In[ ]:





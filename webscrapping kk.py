#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs  


# In[2]:


import requests


# In[3]:


link="https://www.flipkart.com/apple-iphone-13-starlight-128-gb/p/itmc9604f122ae7f?pid=MOBG6VF5ADKHKXFX&lid=LSTMOBG6VF5ADKHKXFXZVXGTL&marketplace=FLIPKART&q=iphone+13&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&fm=organic&iid=30596234-62fa-40b6-b7d2-f958799db637.MOBG6VF5ADKHKXFX.SEARCH&ppt=hp&ppn=homepage&ssid=ddaqy1h6eo0000001666001663490&qH=c68a3b83214bb235"


# In[4]:


requests.get(link)


# In[5]:


page = requests.get(link)


# In[6]:


soup=bs(page.content,"html.parser")
soup


# In[7]:


print(soup.prettify())


# In[8]:


title=soup.title


# In[9]:


print(type (soup))


# In[10]:


print (type(title))


# In[11]:


print (title.string)


# In[12]:


price=soup.find_all("div",class_="_30jeq3 _16Jk6d")
print(price)


# In[13]:


product_price=[]
for i in range (0,len(price)):
    product_price.append(price[i].get_text())
product_price


# In[14]:


name=soup.find_all("p",class_="_2sc7ZR _2V5EHH")
name


# In[15]:


customer_name=[]
for i in range (0,len(name)):
    customer_name.append(name[i].get_text())
customer_name


# In[16]:


comments=soup.find_all("p",class_="_2-N8zT")
comments


# In[18]:


customer_comments=[]
for i in range (0,len(comments)):
    customer_comments.append(comments[i].get_text())
customer_comments


# In[21]:


stars=soup.find_all("div",class_="_3LWZlK _1BLPMq")
stars


# In[23]:


customer_stars=[]
for i in range(0,len(stars)):
    customer_stars.append(stars[i].get_text())
customer_stars


# In[25]:


reviews=soup.find_all("div",class_="t-ZTKy")
reviews


# In[26]:


customer_reviews=[]
for i in range(0,len(reviews)):
    customer_reviews.append(reviews[i].get_text())
customer_reviews


# In[28]:


import pandas as pd


# In[29]:


df=pd.DataFrame()
df["Customer_Name"]=customer_name
df["Comment"]=customer_comments
df["Review"]=customer_reviews
df["Stars"]=customer_stars
df


# In[ ]:





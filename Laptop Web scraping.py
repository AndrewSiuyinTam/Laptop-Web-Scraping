#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[77]:


# I will be scraping a laptop catalog from Walmart Website


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests

contents = urlopen("https://www.walmart.com/browse/electronics/google-chromebooks/3944_3951_1089430_1230091_1103213").read()
soup = BeautifulSoup(contents)
containers = soup.findAll("li", {"class":"Grid-col u-size-6-12 u-size-1-4-m u-size-1-5-xl search-gridview-first-grid-row-item"})
print(len(containers))
column = ['Number','Name','Price','Shipping Details','Product Rating']
Result = pd.DataFrame(columns=column)
laptop_name =soup.findAll("div",{"class": "search-result-product-title gridview"})
laptop_price= soup.findAll("span",{"class":"search-result-productprice gridview enable-2price-2"})
shipping_details=soup.findAll("div",{"class":"search-result-product-shipping-details gridview"})
product_rating=soup.findAll("div",{"class":"search-result-product-rating"})

Result['Price']=  [float((re.findall('(\d+\.\d{1,2})', x.text))[0]) for x in laptop_price[0:]]
Result['Name']=[(re.findall('.*', x.text.strip('Product Title')))[0] for x in laptop_name[0:]]
Result['Number'] = range(1, 1+len(Result))
Result['Shipping Details']=[(re.findall('.*', x.text))[0] for x in shipping_details[0:]]
Result['Product Rating']=[(re.findall('.*', x.text))[0] for x in product_rating[0:]]
Result



# coding: utf-8

# _pip install wikitables_ from bash

# In[33]:

from wikitables import import_tables
tables = import_tables('Academy Award for Best Picture')
print(tables[0].name)


# In[34]:

tables[0].rows


# In[36]:

for row in tables[0].rows:
    print '{Film}:{Producer(s)}'.format(**row)


# In[50]:

tables = import_tables('List of pies, tarts and flans')
print(tables[0].name) 


# In[51]:

tables[0].rows


# In[53]:

for row in tables[0].rows:
    print '{Name} is a {Type} dish original from {Origin}.'.format(**row)


# Note that it does not work with all the articles on wikipedia. But it's really cool to play with.

# In[ ]:




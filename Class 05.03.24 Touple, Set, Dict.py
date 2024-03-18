#!/usr/bin/env python
# coding: utf-8

# In[9]:


colors = ('red', 'blue', 'green', 'black', 'pink')
a = ('orange',)
colors = colors + a
print(colors)

colors = list(colors)
colors.append("yellow")
colors.insert(0,'purple')
colors = tuple(colors)
print(colors)


# In[22]:


aset = {0, 1, 2, True, "kaniz", 20.0, "ferdous"}
print(aset)

num = [1, 2, 4.0, 5, 4, 3.47, 2, 8]
num = set(num)
print(num)

num.add(50)
num.remove(4.0)
print(num)
num.pop()
print(num)


# In[36]:


a = {1, 2, 3, 4, 5, 6}
b = {2, 3, 4, 6, 7}
c = a.union(b)
d = a | b
e = a or b
print(c, d, e)

f = a.intersection(b)
g = a & b
h = a and b
print(f, g, h)


# In[59]:


a_Dict = { "name": "kaniz", 'alist' : [0,1,2,[3,4,5],5,6], "color": "red", "num" : 22}

print(a_Dict['alist'][3])
print(a_Dict['alist'][3][1])

a_Dict["name"] = "ferdous"
print(a_Dict)
a_Dict.update({"name" : "binte"})
a_Dict.update({"id" : 5})
a_Dict.pop("alist")
print(a_Dict)


# In[ ]:





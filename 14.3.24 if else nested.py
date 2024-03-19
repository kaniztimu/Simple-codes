#!/usr/bin/env python
# coding: utf-8

# In[6]:


a = 8
if a <= 50:
    if a >= 8:
        if a == 8:
            print("ok")
        else:
            print("not ok")
    else:
        print("not okk")
else:
    print("not okkk")


# In[9]:


#leap year rules:

year = int(input("Enter a year: ", ))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")


# In[10]:


#single line condition:

a = 10
if a%2 == 0: print("Okay"), print("Done")


# In[14]:


a = 0

while a <= 10:
    print(a)
    a += 1


# In[ ]:





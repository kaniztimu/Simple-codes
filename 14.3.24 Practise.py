#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = float(input("Enter your mark : "))
if(a<50 and a>=0):
    print("F")
elif(a>=50 and a<=59):
    print("E")
elif(a>=60 and a<=69):
    print("D")
elif(a>=70 and a<=79):
    print("C")
elif(a>=80 and a<=89):
    print("B")
elif(a>=90 and a<=100):
    print("A")
else:
    print("No result")


# In[2]:


a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
if (a>b):
    print("First is greater")
elif (a<b):
    print("Second is greater")
else:
    print("The numbers are equal")


# In[6]:


#even odd
a = 12

if a%2 == 0:
    print("Even")
else:
    print("Odd")


# In[ ]:





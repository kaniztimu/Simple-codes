#!/usr/bin/env python
# coding: utf-8

# In[5]:


num = int(input("Enter number: ", ))
if num%5 == 0:
    print("Hello")
else:
    print("Bye")


# In[13]:


unit = int(input("Enter unit: ", ))

if unit<=100:
    print("Rs", unit)
    
elif unit>100 and unit<=200:
    next2 = (unit - 100)*5
    print("Rs", next2)
    
elif unit>200:
    next2 = 100*5
    next3 = (unit - 200)*10
    total = next3 + next2
    print("Rs", total)


# In[17]:


#num = int(input("Enter number: ", ))
#print(num%10)

num = input("Enter number: ", )
print(int(num[-1]))


# In[20]:


num = input("Enter number: ", )
last_value = int(num[-1])

if last_value%3 == 0:
    print("Divisible")
else:
    print("Not divisible")


# In[28]:


marks = float(input("Enter your marks: ", ))

if marks>90:
    print("A")
elif marks>=80 and marks<=90:
    print("B")
elif marks>=60 and marks<80:
    print("C")
elif marks<60:
    print("D")    


# In[31]:


year = int(input("Enter year: ", ))
if year%4 == 0:
    print("Leap year")
else:
    print("Not leap year")


# In[33]:


adict = {1 : "Saturday", 2 : "Sunday", 3:"Monday", 4:"Tuesday", 5:"Wednesday", 6:"Thursday", 7:"Friday"}
num = int(input("Enter year: ", ))
if num>=1 and num<=7:
    print(adict[num])
else:
    print("Invalid")


# In[ ]:





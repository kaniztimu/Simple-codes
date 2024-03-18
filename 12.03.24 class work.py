#!/usr/bin/env python
# coding: utf-8

# In[11]:


try:
    adict = {"comilla" : 500, "chittagong" : 1000, "rajshahi": 1200}
    a = input("Enter city name:", )

    if a in adict:
        print("please pay", adict[a], "taka")
    else:
        print("district not found")
        
except Exception:
    print("Invalid")


# In[18]:


salary = int(input("Enter salary: ", ))
year = int(input("Enter year: ", ))

if year >= 5:
    salary = salary + ((salary*5)/100)
    print("Salary is", salary)
    
else:
    print("No bonus", salary)


# In[ ]:





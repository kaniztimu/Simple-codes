#!/usr/bin/env python
# coding: utf-8

# In[21]:


try:
    number1 = int(input("Enter 1st number: ", ))
    number2 = int(input("Enter 2nd number: ", ))
    operation = input("Enter operation: ", )            

    if operation == "+":
        print(number1+number2)
    elif operation == "-":
        print(number1-number2)
    elif operation == "*":
        print(number1*number2)
    elif operation == "/":
        print(number1/number2)
        
except Exception:
    print("Invalid")


# In[ ]:





# In[ ]:





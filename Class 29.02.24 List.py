#!/usr/bin/env python
# coding: utf-8

# In[38]:


flowers = ["Rose", "Sunflower", "Dalia", "Lotus", "Lily", "Hasnahena"]
print(len(flowers))
print(type(flowers))
print(flowers[:])
print(flowers[::])
print(flowers[0:-1])
print(flowers[:-1])
print(flowers[2:-2])
print(flowers[::4], "\n")

print(sorted(flowers))
flowers.sort()
print(flowers)
flowers.reverse()
print(flowers, "\n")

flowers.append("Merigold")
print(flowers)
flowers.insert(2, "Daisy")
print(flowers, "\n")

flowers.remove("Rose")
print(flowers)
flowers.pop()
print(flowers)
flowers.pop(2)
print(flowers)


# In[ ]:





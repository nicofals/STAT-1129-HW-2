#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = 0
while n < 10:
    if n == 5:
        break
    print(n)
    n += 1


# In[2]:


n = 0
while n < 5:
    print(n)
    n += 1
if n >= 5:
    print(f"{n} is not less than 5")


# In[4]:


fruits = ['pear', 'passionfruit', 'apple', 'mango']
for fruit in fruits:
    if fruit == 'apple':
        print(f"{fruit} is really a fruit?")
        break
    else:
        print(f"I like {fruit}")


# In[5]:


n = 1
total = 0
while n <= 30:
    total += n
    n += 1
print(total)


# In[6]:


grade = 61

if grade >= 90:
    print("The grade is A.")
elif grade >= 80:
    print("The grade is B.")
elif grade >= 70:
    print("The grade is C.")
elif grade >= 60:
    print("The grade is D.")
else:
    print("The grade is F.")


# In[7]:


marks = {'Andy': 88, 'Amy': 66, 'James': 90, 'Jules': 55, 'Arthur': 77}

for name, grade in marks.items():
    print(name + "," + str(grade))


# In[8]:


marks = {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}
mean_grade = sum(marks.values()) / len(marks)
print(mean_grade)
max_grade = max(marks.values())
print(max_grade)
min_grade = min(marks.values())
print(min_grade)


# In[9]:


marks = {'Andy': 88, 'Amy': 66, 'James': 90, 'Jules': 55, 'Arthur': 77}
for key in marks:
    if 'J' in key:
        break
    print(key)


# In[10]:


marks = {'Andy': 88, 'Amy': 66, 'James': 90, 'Jules': 55, 'Arthur': 77}
for key in marks:
    if 'J' in key:
        continue
    print(key)


# In[ ]:





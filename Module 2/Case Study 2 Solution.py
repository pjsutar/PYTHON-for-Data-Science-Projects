#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))


# In[2]:


#Q2
d ={"john":40, "peter":45}
print(list(d.keys()))


# In[3]:


#Q3
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")


# In[4]:


#Q4
a = [4,7,3,2,5,9]

for i in a:
    print("Element: " + str(i) + " Index: "+ str(a.index(i)))


# In[6]:


#Q5
def odd_values_string(str):  
  result = ""   
  for i in range(len(str)):  
    if i % 2 == 0:  
      result = result + str[i]  
  return result  
  
print(odd_values_string('H1e2l3l4o5w6o7r8l9d'))


# In[7]:


#Q6
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


# In[8]:


#Q7
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('abcdefgabc'))


# In[9]:


#Q8
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
   
lst1 = [1, 3, 6, 78, 35, 55] 
lst2 = [12, 24, 35, 24, 88, 120, 155] 
print(intersection(lst1, lst2))


# In[12]:


#Q9
list = [12, 24, 35, 24, 88, 120, 155]
list = [x for (i,x) in enumerate(list) if i not in (1,3)]
print(list)


# In[13]:


#Q10
list = [12, 24, 35, 24, 88, 120, 155]
list = [x for (i,x) in enumerate(list) if i not in (0,4,5)]
print(list)


# In[19]:


#Q11
list = [12, 24, 35, 24, 70, 88, 120, 155]
list = [x for x in list if x%5 == 0 and x%7 == 0]
print(list)


# In[20]:


#Q12
n=int(input("Enter the number of terms: "))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)+(i/i+1)
print("The sum of series is",round(sum1,2))


# In[ ]:





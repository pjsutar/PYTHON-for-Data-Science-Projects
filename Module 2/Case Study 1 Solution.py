#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Problem 1
# Step 2: To find factors of a number.
def print_factors(x):
    print("The factors of",x,"are")
    for i in range(1, x+1):
        if x % i == 0:
            print(i)
num = 200
print_factors(num)


# In[11]:


# Step 2: To recognize whether the factors are even or odd.
num = int(input("The factor to check: "))
if num % 2 == 0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))


# In[12]:


# Problem 2: Sorting the words alphabetically
my_str = input("Enter a string: ")
words = my_str.split()
words.sort()
print("The sorted words are: ")
for word in words:
    print(word)


# In[3]:


# Problem 3
items = []
for i in range(1000, 3000):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        items.append(s)
print(",".join(items))


# In[4]:


# Problem 4
s = input("Enter a string")
d=l=0
for c in s:
    if c.isdigit():
        d = d+1
    elif c.isalpha():
        l = l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


# In[6]:


# Problem 5: To find a number is palindrome or not
num = input("Enter a number: ")
try:
    val = int(num)
    if num == str(num) [::-1]:
        print("The given number is Palindrome")
    else:
        print("The given number is not a Palindrome")
except ValueError:
    print("That's not a valid number, Try Again!")
    


# In[ ]:





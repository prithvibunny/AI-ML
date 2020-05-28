#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Generate the following pattern

rows = int(input("Enter number of rows "))
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')

    print("\r")


# In[2]:


# 2. Display multiplication table of K. Take k value from user

num = int(input("Enter number"))
for i in range(1,11):  
   print(num,'x',i,'=',num*i)  


# In[4]:


# 3. Roots of quadratic equation

import cmath

a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution is {0} and {1}'.format(sol1,sol2))


# In[11]:


# 4. Convert a decimal number to Binary

number = int(input("Enter any decimal number: "))
print("Equivalent Binary Number: ", bin(number))


# In[16]:


# 5. Generate first N number of Fibonacci numbers.

def printFibonacciNumbers(n): 
    f1 = 0
    f2 = 1
    if (n < 1): 
        return
    for x in range(0, n): 
        print(f2, end = " ") 
        next = f1 + f2 
        f1 = f2 
        f2 = next

printFibonacciNumbers(7) 


# In[ ]:





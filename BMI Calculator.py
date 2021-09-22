#!/usr/bin/env python
# coding: utf-8

# In[1]:


weight = float(input('Enter your weight(in kilograms): '))

height = float(input('Enter your height(in metres): '))

bmi = weight / (height ** 2)

print('Your body mass index is ', bmi, 'kg/m^2')
if bmi < 18.5 :

  print('This is considered underweight')

elif 18.5 <= bmi < 25:

  print('This considered healthy')

elif 25 <= bmi < 30:

  print('This is considered overweight')

else:

  print('This is considered obese')


# In[ ]:





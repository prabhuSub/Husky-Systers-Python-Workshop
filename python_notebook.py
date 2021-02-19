#!/usr/bin/env python
# coding: utf-8

# ## Index
# 1. How to run a Python code
# 2. Variables
# 3. Data types
#     - Strings
#     - Lists
#     - Booleans
#     - Dictionaries
#     - Tuples
#     - Sets
# 4. For Loops
# 5. Functions
# 6. Parameters and Arguments
# 7. Docstrings
# 8. Clean Code
# 9. Object Oriented Programming – OOPs
# 10. Lambda Expressions
# 11. Errors Handling in Python
# 

# ## How to run a Python code
# 
# Multiple ways to run a code based on my experience:
# Using tools like:
# 
# 1. Notebooks - Jupyter Notebook, JupyterLab
# 2. IDE - Visual Studio Code, PyCharm, Spyder, etc
# 3. Terminal

# ## Variables

# In[1]:


user_name = 'Prabhu Subramanian'
age = 25
PI_CONSTANT = 3.14
_variable_ = 'Test'


# In[2]:


__not_used__ = 'DO NOT USE SUCH VARIABLES'


# ## Data Types

# ### String

# In[3]:


# Strings
first_name = 'Prabhu'
second_name = 'Subramanian'

# lets concatinate two strings
print(type(first_name + second_name))


# ### List

# In[4]:


# List
movie_list = list() # initiate a list object
movie_list.append('The Equilizer') # appending first element to it
movie_list.append('Ipman') # append second element to it
print(movie_list)
print(type(movie_list))


# ### Boolean

# In[5]:


# Boolean
validate = bool() # by default the boolean object will initate as False
validate = True
print(validate)
print(type(validate))

# lets use it for if condition to see if we can get inside the condition
if validate: 
    print("It is validated")


# ### Dictionaries

# In[6]:


# Dictionaries
dict_variable = dict()
# disctionaries are key-value pair
dict_variable['key1'] = 'value1'
dict_variable['key2'] = 'value2'
print(dict_variable)
print(type(dict_variable))


# ### Tuples

# In[7]:


# Tuples
tuple_variable = ('Prabhu', 'Subramanian', 27)
print(tuple_variable)
print(type(tuple_variable))

# using tuples we print the relavant data stored in them by accessing the elements
print('First Name: ' + tuple_variable[0])
print('Second Name: ' + tuple_variable[1])
# print('Age: ' + tuple_variable[2])


# ### Sets

# In[8]:


# Sets
set_variable = set()
set_variable.add(1)
set_variable.add(2)
set_variable.add(3)
set_variable.add(4)
set_variable.add(5)
print('first print: ' + str(set_variable))

# adding a value again to the set
set_variable.add(5)
print('second print: ' + str(set_variable))


# In[9]:


# Lets try working on some problem

''' Subtract an element from two lists
    and find the uncommon elements between the both
'''
list_1 = [1,3,5,6]
list_2 = [1,5,7,8]
uncommon_elements = list(set(list_1) - set(list_2)) # list(set(list_2) - set(list_1))
print(uncommon_elements)


# In[17]:


# copying a list

list_3 = list_1[:]
print(list_3)


# In[18]:


list_3[2] = 5
print(list_1)
print(list_3)


# In[21]:


# Difference between `is` and `==`
print(True == 1)
print([] == [])
print(1 == '1')
print(10 == 10.0)
print('**********')
a = [1,2,3]
b = a
print(a is b)


# ## For loops

# In[22]:


# For loops description
for items in list_1:
    print(items)


# In[24]:


# one line for loop, which returns a value for your use
x = [1, 2, 3, 4, 5]
y = [a for a in x if a % 2 == 1]
print(y)


# In[27]:


# iterate through dictionaries
dictionary = {
    'one': 1,
    'two': 2,
    'three': 3
}
for key,value in dictionary.items():
    print(key, value)


# ## Functions

# In[34]:


# defining a function
def say_hello(name, age):
    print(f'Hello {name} {age}')
    
# calling the function
say_hello('Prabhu', 27) 
say_hello('Prabhu', '😊')


# In[37]:


# clean the code:
def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False

# calling the method to check
is_even(51)


# ## Parameters and arguments

# In[43]:


# Use of *args and **kwargs
def sum_function(*args, **kwargs):
    '''Explain what are *args and *kwargs
    '''
    print(f'AGRS: {args}')
    print(f'KWARGS: {kwargs}')
    
    return sum(args) + (kwargs['divident']/kwargs['divisor'])

# call the function to see the return value
sum_function(1,2,3,4,5,divident=10,divisor=2)


# ## Docstrings
# 
# Will be explained with an example

# ## Clean code
# 
# Examples will be shown and discussed

# ## Object Oriented Programming – OOPs
# 
# Will be explained with an example

# In[48]:


# lets create a class for an Object:
class Person:
    year = 2021
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def details(self):
        ''' Print the detials of the person
        '''
        print(f'NAME: {name}')
        print(f'AGE: {age}')
        print(f'HEIGHT: {height}')


# In[49]:


person_1 = Person('Prabhu', 27, '6\'1\"')
print(person_1.name)
print(person_1.age)
print(person_1.height)
print(person_1.year)


# ## Lambda expressions

# In[65]:


def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))


# ## Errors Handling in Python

# In[68]:


# It is all about using try except like try catch in JAVA
def function(num1, num2):
    try:
        return sum(num1, num2)
    except TypeError:
        print('Please provide number as a parameter')

function(1,'2')


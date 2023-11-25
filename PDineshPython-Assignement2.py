#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Create your own lists otherwise use the List1 =
get_ipython().run_line_magic('pinfo', 'Operations')

A. Repetition (\*)

B. Concatenation (+)

C. Membership

D. Length

E. Iteration


# In[2]:


List1 =['hello','GUVI','GEEK']
Rept=List1*3
Rept


# In[4]:


List1 =['hello','GUVI','GEEK']
List2 =['hello','Welcome','To','GUVI']
Concatenation=List1+List2
Concatenation


# In[6]:


List1 =['hello','GUVI','GEEK']
print('hello' in List1)


# In[9]:


List1 =['hello','GUVI','GEEK']
len(List1)


# In[10]:


List1 =['hello','GUVI','GEEK']
for i in List1:
    print(i)


# In[ ]:


Create your own lists to perform the below Python List Built-in
get_ipython().run_line_magic('pinfo', 'functions')

otherwise use the

List1 = [15, 300, 2700, 821]

List2 = [12, 2]

List3 = [34, 567, 78]

A. max(list)

B. min(list)

C. list(seq)


# In[11]:


List1 = [15, 300, 2700, 821]
max(List1)


# In[12]:


List2 = [12, 2]
min(List2)


# In[15]:


List3 = [34, 567, 78]
list(List3)


# In[17]:


List4= 'Dinesh'
list(List4)


# In[ ]:


3. Create your own lists to perform the below Python List built-in
methods

A. list.append()

B. list.clear()

C. List.copy()

D. list.count()

E. list.extend()

F. list.index()

G. list.insert()

H. list.pop()

I. list.remove()

J. list.reverse()

K. list.sort()


# In[22]:


List =['hello','GUVI','GEEK']
List.append('Dinesh')
List


# In[24]:


List1 =['hello','GUVI','GEEK']
List1.clear()
List1


# In[28]:


List1 =['hello','GUVI','GEEK']
List2= List1.copy()
print('Old list:', List1)
print('New List:', List2)


# In[29]:


List1 =['hello','GUVI','GEEK']
List1.count('hello')


# In[1]:


List1 =['hello','GUVI','GEEK']
List2 =['hello','Welcome','TO','GUVI']
List1.extend(List2)
print(List1)


# In[2]:


List1 =['hello','GUVI','GEEK']
List1.index('GEEK')


# In[4]:


List1 =['hello','GUVI','GEEK']
List1.insert(2,'DINESH')
print(List1)


# In[6]:


List1 =['hello','GUVI','GEEK']
list=List1.pop(2)
print(list)
print(List1)


# In[8]:


List1 =['hello','GUVI','GEEK']
List1.remove('GUVI')
print(List1)


# In[9]:


List1 =['hello','GUVI','GEEK']
List1.reverse()
List1


# In[10]:


List=[2,33,243,4533,454,5577,8975,3453,1]
List.sort()
print(List)


# In[ ]:


Create your own Tuple to perform the below Python tuple Operations ?

otherwise use the below

Tuple1 = ('a','b','c','d')

Tuple2 = ('e','f','g','h')

 Tuple Operations

A. Repetition (\*)

B. Concatenation (+)

C. Membership

D. Length

E. Iteration


# In[12]:


Tuple1 = ('a','b','c','d')*3
print(Tuple1)


# In[13]:


Tuple1 = ('a','b','c','d')

Tuple2 = ('e','f','g','h')

Tuple=Tuple1+Tuple2
print(Tuple)


# In[14]:


Tuple1 = ('a','b','c','d')
print('c' in Tuple1)


# In[15]:


Tuple1 = ('a','b','c','d')
print('g' in Tuple1)


# In[17]:


Tuple1 = ('a','b','c','d')
len(Tuple1)


# In[18]:


for i in Tuple1:
    print(i)


# In[ ]:


Create your own Tuple to perform the below Python tuple inbuilt
functions ?

otherwise use the below

Tuple1 =
(1,4,2,4,5,6,3,5,4,6,77,8,7,7,876,89,8765,4,5,1,876,9,3456,4234)

A. max(Tuple)

B. min(Tuple)

C. Tuple(seq)


# In[23]:


Tuple1 =(1,4,2,4,5,6,3,5,4,6,77,8,7,7,876,89,8765,4,5,1,876,9,3456,4234)
max(Tuple1)


# In[24]:


Tuple1 =(1,4,2,4,5,6,3,5,4,6,77,8,7,7,876,89,8765,4,5,1,876,9,3456,4234)
min(Tuple1)


# In[28]:


Tuple1 =(1,4,2,4,5,6,3,5,4,6,77,8,7,7,876,89,8765,4,5,1,876,9,3456,4234)
tuple(Tuple1)


# In[30]:


Tuple1 ='querty'
tuple(Tuple1)


# In[ ]:


Create your own Set to operate the below Python Set Operations ?

otherwise use the below set:

Set1 = {1,4,2,4,5,6,3,5,4,6,77,8,7,7,876}

Set2 = {3,432,5,6,4,6,7,6,5,6,54,567,5}

Set Operations

A. Union

B. Intersection

C. Difference

D. Symmetric difference


# In[33]:


Set1 = {1,4,2,4,5,6,3,5,4,6,77,8,7,7,876}

Set2 = {3,432,5,6,4,6,7,6,5,6,54,567,5}

print(Set1 | Set2)


# In[34]:


Set1 = {1,4,2,4,5,6,3,5,4,6,77,8,7,7,876}

Set2 = {3,432,5,6,4,6,7,6,5,6,54,567,5}

print(Set1&Set2)


# In[35]:


Set1 = {1,4,2,4,5,6,3,5,4,6,77,8,7,7,876}

Set2 = {3,432,5,6,4,6,7,6,5,6,54,567,5}
print(Set1^Set2)


# In[ ]:


Create your own Dictionary to perform the below Python Built-in
Dictionary functions

otherwise use the below Dictionary:

dict = {'Name': 'Student', 'Age': 27};

A. len(dict)

B. str(dict)

C. type(variable)


# In[36]:


dict = {'Name': 'Student', 'Age': 27}
len(dict)


# In[37]:


dict = {'Name': 'Student', 'Age': 27}
str(dict)


# In[38]:


dict = {'Name': 'Student', 'Age': 27}
type(dict)


# In[ ]:


Create your own Dictionary to perform the below Python Built-in
Dictionary methods

otherwise use the below Dictionary:

dictionaries = {0:" Data",1: "GUVI", 2: "GEEK",3:"Python",4:"Happy"}

A. dic.clear()

B. dict.copy()

C. dict.fromkeys()

D. dict.get(key[, value])

E. dict.items()

F. dict.keys()

G. dict.setdefault()

H. dict.update()

I. dict.values()


# In[40]:


dictionaries = {0:" Data",1: "GUVI", 2: "GEEK",3:"Python",4:"Happy"}
dictionaries.clear()
dictionaries


# In[41]:


dictionaries = {0:" Data",1: "GUVI", 2: "GEEK",3:"Python",4:"Happy"}
new=dictionaries.copy()
print(dictionaries)
print(new)


# In[49]:


dictionaries = {" Data","GUVI","GEEK","Python","Happy"}
dict=dict.fromkeys(dictionaries)
print(str(dict))
dict=dict.fromkeys(dictionaries,10)
print(str(dict))


# In[53]:


dictionaries = {'Name':'Dinesh', 'Age' : 30}
print('Name:',dictionaries.get('Name'))
print('Age:',dictionaries.get('Age'))
print('Salary:',dictionaries.get('Salary'))
print('Salary:',dictionaries.get('Salary', "Not Found!"))


# In[54]:


sales={'apple':1,'Orange':30,'Grapes':140}
print(sales.items())


# In[55]:


sales={'apple':1,'Orange':30,'Grapes':140}
print(sales.keys())


# In[62]:


sales={'apple':1,'Orange':30,'Grapes':140}
print(sales.keys())
print(sales.values())
print(sales.items())

fruit=sales.setdefault('fruit')
print('sales=',sales)
print('fruit=',fruit)

fruit1=sales.setdefault('fruit1',3)

print('sales=',sales)
print('fruit1',fruit1)


# In[65]:


sales={'apple':1,'Orange':30,'Grapes':140}
sales1={'Banana':40,'Pineapple':44}
print('Before update:',sales)
sales.update(sales1)
print('After update:',sales)


# In[69]:


sales={'apple':1,'Orange':30,'Grapes':140}
print(sales.values())
sales['Orange']


# In[ ]:


# Conditional Statements

1. IF

2. IF-ELSE

3. If...Elif...Else

1. Write if statement 13 is greater than 25?

2. Write a if else statement to find if the number is divisible by 25?

3.Using the three variables 'a = 154; b = 2451; c = 6054',

Write a If...Elif...Else statement to find the greatest number


# In[70]:


Write if statement 13 is greater than 25?


# In[74]:


if(13>25):
    print("13 is less than 25")


# In[ ]:


Write a if else statement to find if the number is divisible by 25?


# In[80]:


n=input()
if int(n)%25==0:
    print("N is divisible by 25")
else:
    print("N is not divisible by 25")
    


# In[ ]:


Using the three variables 'a = 154; b = 2451; c = 6054',

Write a If...Elif...Else statement to find the greatest number


# In[81]:


a = 154; b = 2451; c = 6054
if(b<=a) and (b<=c):
    print('b is greater number')
elif(a>=c) and (a>=b):
    print('a is greater number')
else:
    print('c is greater number')
    
    


# In[ ]:





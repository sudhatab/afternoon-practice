#!/usr/bin/env python
# coding: utf-8

# In[41]:


#Lambda Excercise 1

#Consider the List

prog_lang = [('Python', 3.8),
    ('Java', 13),
    ('JavaScript', 2019),
    ('Scala', 2.13)]


#1. Sort the list by each language's version in ascending order.
#[('Scala', 2.13), ('Python', 3.8), ('Java', 13), ('JavaScript', 2019)]

lst = sorted(prog_lang, key=lambda x:x[1])
print(lst)

#2. Sort the list by the length of the name of each language in descending order.
#[('JavaScript', 2019), ('Python', 3.8), ('Scala', 2.13), ('Java', 13)]


lst1 = sorted(prog_lang, key=lambda x: len(x[0]), reverse=True)
print(lst1)
                 
#3. Filter the list so that it only contains languages with 'a' in it.
#[('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]

lst2 = list(filter(lambda x:'a' in x[0], prog_lang))
print(lst2)

#4. Filter the list so that it only contains languages whose version is in integer form.
#[('Java', 13), ('JavaScript', 2019)]

lst3 = list(filter(lambda x: type(x[1])==int, prog_lang))
print (lst3)

#5. Transform the list so that it contains the tuples in the form,
#("language in all lower case", length of the language string)
#[('python', 6), ('java', 4), ('javascript', 10), ('scala', 5)]

tt = list(map(lambda x: (x[0].lower(), len(x[0]) ), prog_lang))
print(tt)

#6. Generate a tuple in the form,
#("All languages separated by commas","All versions separated by commas")
#('Python,Java,JavaScript,Scala', '3.8,13,2019,2.13')

from functools import reduce
r = reduce(lambda a, b: (a[0]+ ", " +b[0], str(a[1])+ ", " +str(b[1]) ), prog_lang)
print(r)


# In[ ]:





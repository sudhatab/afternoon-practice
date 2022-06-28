#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.
def primes_gen(n):
    for i in range(2,n):
        for t in range(2,i):
            if i%t == 0:
                break
            else:
                yield i
                
             
gen = primes_gen()
for n in range(10):
    print(next(gen), end=' ')
# Expected output
# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------
#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.
def unique_letters(word):
    done = []
    for c in word:
        if c not in done:
            yield c
            done.append(c)
            
for letter in unique_letters('hello'):
    print(letter, end=' ')
# Expected output
# h e l o


# In[ ]:





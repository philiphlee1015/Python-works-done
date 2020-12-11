## File: phl6cw-assignment01.py 
## Topic:  Assignment 01 Solutions
## Name: Philip Lee

## 1.  For the questions in this part, use the following
##     lists as needed:
list01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
list02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1,0,5]
list03 = [2,-5,6,7,-2,-3,0,3,0,2,8,7,9,2,0,-2,5,5,6]
biglist = list01 + list02 + list03

## (a) Find the product of the last four elements of list02.

import numpy as np
result = np.prod(np.array(list02[-4:]))     #uses np function to get the product of last four elements 
print(result)                               #source: https://stackoverflow.com/questions/13840379/how-can-i-multiply-all-items-in-a-list-together-with-python
"""
## 1(a)

0
"""


## (b) Extract the sublist of list01 that goes from
##     the 3rd to the 11th elements (inclusive).

print(list01[2:11])
"""
## 1(b)

[4, 9, 10, -3, 5, 5, 3, -8, 0]  # sublist
"""

## (c) Concatenate list01 and list03 (in that order), sort
##     the combined list, then extract the sublist that 
##     goes from the 5th to the 15th elements (inclusive).
list04 = list01+list03          ##Concatenates list01 and list03 as list04
list04.sort()                   ##sorts list04
print(list04[4:15])

"""
## 1(c)
[-3, -2, -2, -2, 0, 0, 0, 0, 0, 2, 2]   # the sublist
"""

## (d) Generate "biglist", then extract the sublist of every 4th 
##     element starting with the 3rd element

biglist = list01 + list02 + list03
print(biglist[2::4])            #extracts sublist of every 4th element starting w/3rd element

"""
## 1(d)
[4, 5, 0, 8, 6, -5, 6, 10, -4, 2, -2, 0, 9, 5]
"""

## 2.  Use for loops to do each of the following with the lists
##     defined above.
 
## (a) Add up the squares of the entries of biglist.

s=0
for i in biglist:
    s += i**2
print(s)
"""
## 2(a)

1825           ##sum of the squares of entries in biglist
"""

## (b) Create "newlist01", which has 19 entries, each the 
##     sum of the corresponding entry from list01 added 
##     to the corresponding entry from list02.  That is,
##     
##         newlist01[i] = list01[i] + list02[i] 
##
##     for each 0 <= i <= 18.

newlist01 = 19*[0]
for i in range (19):
    newlist01[i] = list01[i] + list02[i]        #adds the entries in each list to the corresponding entries
print(newlist01)
"""
## 2(b)

[-5, 2, 12, 4, 5, -5, 9, 11, 10, -3, 9, 12, 5, 21, -4, -6, -3, 0, 11]
"""


## (c) Compute the mean of the entries of biglist.
##     (Hint: len(biglist) gives the number
##     of entries in biglist.  This is potentially useful.)

for i in biglist:
    avgbiglist = sum(biglist)/len(biglist)      ## finds the average by getting the total/# of entries
print(avgbiglist)

"""
## 2(c)

2.3684210526315788           ##mean of the entries of biglist
"""


## (d) Determine the number of entries in biglist that
##     are less than 6.

ct = 0 
for b in biglist:
    if b <6 :  
        ct = ct + 1
print(ct)

"""
## 2(d)

40
"""

## (e) Determine the number of entries in biglist that
##     are between -2 and 4 (inclusive).

ct = 0 
for b in biglist:
    if b >= -2 and b <=4 :  
        ct = ct + 1
print(ct)

"""
##2e

22
"""

## (f) Create a new list called "newlist02" that contains 
##     the elements of biglist that are greater than 0.

newlist02 = []
for b in biglist:
    if b > 0:
        newlist02.append(b)
print(newlist02)     

"""
##2f

[2, 5, 4, 9, 10, 5, 5, 3, 2, 3, 8, 8, 6, 8, 4, 6, 7, 5, 9, 10, 2, 13, 1, 5, 2, 6, 7, 3, 2, 8, 7, 9, 2, 5, 5, 6]    
"""

## 3.  In this problem you will be simulating confidence intervals
##     for samples drawn from a uniform distribution on [0,24], 
##     which has a mean of 12.
##     For instance, a sample of size 10 can be drawn with the 
##     commands
import numpy as np # "as np" lets us use "np"; only run once
samp = np.random.uniform(low=0,high=24,size=10)

## (a) Use random samples of size 20 and simulation to generate 
##     500,000 confidence intervals of the form
##                                                          count them and divide it by 500000 and * by 100 to get %
##                           xbar +- 2
## 
##     Use your confidence intervals to estimate the confidence
#      level. (Give the level as a percentage.)

ct = 0
for i in range(500000):                             
    x = np.random.uniform(low=0,high=24,size=20)
    if np.mean(x) < 14 and np.mean(x)>10:                   ##used for confidence interval +-2 based on mean 12
        ct += 1
print(ct/500000*100)

"""
##3a

80.1502          ## confidence level as a percentage
"""

## (b) Repeat (a) with confidence intervals xbar +- 3
ct = 0
for i in range(500000):
    x = np.random.uniform(low=0,high=24,size=20)
    if np.mean(x) < 15 and np.mean(x)>9:
        ct += 1
print(ct/500000*100)

"""
##3b

94.7988
"""

## (c) Repeat (a) with samples of size 30.
ct = 0
for i in range(500000):
    x = np.random.uniform(low=0,high=24,size=30)
    if np.mean(x) < 14 and np.mean(x)>10:
        ct += 1
print(ct/500000*100)

"""
## 3c

88.6228
"""


## (d) Repeat (b) with samples of size 30.
ct = 0
for i in range(500000):
    x = np.random.uniform(low=0,high=24,size=30)
    if np.mean(x) < 15 and np.mean(x)>9:
        ct += 1
print(ct/500000*100)

"""
## 3d

98.2932
"""

## 4.  Here we repeat parts (a)-(d) of #3, but this time using
##     samples from an exponential distribution with mean 12.
##     The code below will produce a sample of size 10 with 
##     mean = 12:
samp = np.random.exponential(scale=12,size=10)
## (a)
ct = 0
for i in range(500000):
    x = np.random.exponential(scale=12,size=20)
    if np.mean(x) < 14 and np.mean(x)>10:
        ct += 1
print(ct/500000*100)

"""
##4a

54.4412
"""

##(b)
ct = 0
for i in range(500000):
    x = np.random.exponential(scale=12,size=20)
    if np.mean(x) < 15 and np.mean(x)>9:
        ct += 1
print(ct/500000*100)

"""
##4b

74.1428
"""

##(c)
ct = 0
for i in range(500000):
    x = np.random.exponential(scale=12,size=30)
    if np.mean(x) < 14 and np.mean(x)>10:
        ct += 1
print(ct/500000*100)

"""
##4c

64.1532
"""

##(d)
ct = 0
for i in range(500000):
    x = np.random.exponential(scale=12,size=30)
    if np.mean(x) < 15 and np.mean(x)>9:
        ct += 1
print(ct/500000*100)

"""
##4d

83.2864
"""
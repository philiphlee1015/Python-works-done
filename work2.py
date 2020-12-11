## 1.
##
## 1(a) Generate an array x of 10000 random values from 
##      a uniform distribution on the interval [0,50],
##      then use a for loop to determine the percentage     
##      of values that are in the interval [8,27].

## Note: 1(a) asks for a percentage, not a count and not
##       a proportion.

import numpy as np
ct=0
x = np.random.uniform(low=0,high=50,size=10000)     ##generates array of x of 10000 random values from a uniform distribution on interval [0,50]
for i in x:
    if i >= 8 and i<=27:         ##uses inequality to find the numbers between 8 and 27 and adds +1 to count when the condition is satisfied
        ct += 1
print(ct/10000*100)

"""
1a

38.32                 ##percentage of values in the interval [8,27]
"""

## 1(b) Repeat 1(a) 1000 times, then compute the average
##      of the 1000 percentages found.

ctarray=np.zeros(1000)      #An array of 1000 zeros for placeholding counts
for i in range(1000):
    x = np.random.uniform(low=0,high=50,size=10000)
    ct = 0
    for xval in x:                  ##repeats part A
        if xval >= 8 and xval<=27:
            ct += 1
    ctarray[i] = ct/10000*100

np.mean(ctarray)        ##finds the mean of the 1000 percentages
    
"""
1b

38.011979999999994        ## mean of 100 percentages in percentage form
"""

## 1(c) For the array x in 1(a), use a while loop to determine 
##      the number of random entries required to find the
##      first that is less than 3.

ct=1            #initializes the counter
x = np.random.uniform(low=0,high=50,size=10000)
i=0         ## used to add 1 to the counter when the condition is satisfied 
            ## and also used to get rid of ambiguity caused by size=10000 when creating uniform distribution
while x[i] >= 3:
    ct +=1
    i +=1       ##adds to the ct
print(ct)

"""
1c

43                ##number of random entries required to find the first that is less than 3
"""

## 1(d) Repeat 1(c) 1000 times, then compute the average for the
##      number of random entries required.
ctarray = np.zeros(1000)  # An array to hold the values of ct
for i in range(1000):
    ct = 1  # Initialize the counter
    bb = 0  # used to add 1 to the counter when the condition is satisfied and also used to get rid of ambiguity
            # of the while loop
    x = np.random.uniform(low=0,high=50,size=10000)  # initial random uniform value
    while x[bb] >= 3:
        ct += 1  # Increment the counter by 1
        bb += 1
    ctarray[i] = ct  # Record the number of selections required

np.mean(ctarray)  # Compute the mean number of selections required


"""
1d

16.451               ##avg number of random entries required
"""


## 1(e) For the array x in 1(a), use a while loop to determine 
##      the number of random entries required to find the
##      third entry that exceeds 36.

x = np.random.uniform(low=0,high=50,size=10000)
ct=0        ##ct=maximum number of successes
ct2=0       ##ct2 = number of trials needed to get to the maximum number of successes
i=0         ## i = index holder
while(ct<3):            ##repeats the loop until it reaches max number of successes
    if x[i]<=36:        ##condition for failure. ct2 increases to count the number of trials/entries
        ct2 +=1 
        i +=1           ##index holder used to move up the counts up for the x
    else:               ##condition for success. ct2 increases to count the number of trials/entries
        ct+=1           ##ct increases by 1 when the entry exceeds 36 and goes back to the while loop to
        ct2 +=1         ##repeat the processes until ct reaches 3
        i +=1
print(ct2)

"""
1e

12             ##number of random entries required to find the third entry that exceeds 36
"""


## 1(f) Repeat 1(e) 5000 times, then compute the average for the
##      number of random entries required.
ctarray = np.zeros(5000)
for j in range(5000):
    x = np.random.uniform(low=0,high=50,size=10000)
    ct=0            ##ct= maximum number of successes
    ct2=0           ##ct2= number of trials needed to get to the maximum number of successes
    i=0             #i = index holder
    while(ct<3):        ##same code as 1e
        if x[i]<=36:
            ct2 +=1     
            i +=1
        else:
            ct+=1
            ct2 +=1
            i +=1
    ctarray[j]=ct2              ##holds the 5000 ct2 values
    
np.mean(ctarray)            ##finds the mean of the 5000 ct2 values


"""
1f

10.6216           ##avg number of random entries required to find the third entry that exceeds 36
"""


## 2.   For this problem you will draw samples from a normal
##      population with mean 40 and standard deviation 12.
##      Run the code below to generate your population, which
##      will consist of 1,000,000 elements.

import numpy as np 
p1 = np.random.normal(40,12,size=1000000)

## 2(a) The formula for a 95% confidence interval for the 
##      population mean is given by
##     
##      [xbar - 1.96*sigma/sqrt(n), xbar + 1.96*sigma/sqrt(n)]
##
##      where xbar is the sample mean, sigma is the population
##      standard deviation, and n is the sample size.
##
##      Select 10,000 random samples of size 10 from p1.  For
##      each sample, find the corresponding confidence 
##      interval, and then determine the percentage of
##      confidence intervals that contain the population mean.
##      (This is an estimate of the confidence level.)

ct = 0  # counter for successes
n = 10 # the sample size
p = np.mean(p1)  # The true mean of population
sigma=12
for i in range(10000):
    s = np.random.choice(p1, size=10) # Generate a random sample
    xbar = np.mean(s)  # compute sample mean
    lcl = xbar - 1.96*sigma/np.sqrt(n) # lower conf. limit
    ucl = xbar + 1.96*sigma/np.sqrt(n)# upper conf. limit
    if lcl <= p and ucl >= p:
        ct += 1
print(ct/10000)


"""
2a

0.9456       ## percentage in decimal form
94.5         ## answer in percentage form
"""


## 2(b) Frequently in applications the population standard
##      deviation is not known. In such cases, the sample
##      standard deviation is used instead.  Repeat part 2(a)
##      replacing the population standard deviation with the
##      standard deviation from each sample, so that the
##      formula is
##
##      [xbar - 1.96*stdev/sqrt(n), xbar + 1.96*stdev/sqrt(n)]
##
##      Tip: Recall the command for the standard deviation is 
##           np.std(data, ddof=1)

ct = 0  # counter for successes
n = 10 # the sample size
p = np.mean(p1)  # The true mean our population
for i in range(10000):
    s = np.random.choice(p1, size=10) # Generate a random sample
    xbar = np.mean(s)  # compute sample mean
    lcl = xbar - 1.96*np.std(s, ddof=1)/np.sqrt(n) # lower conf. limit
    ucl = xbar + 1.96*np.std(s, ddof=1)/np.sqrt(n)# upper conf. limit
    if lcl <= p and ucl >= p:
        ct += 1
ct/10000

"""
2b

0.9198         ## percentage in decimal form
91.98          ## answer in percentage form
"""



## 2(c) Your answer in part 2(b) should be a bit off, in that
##      the estimated confidence level isn't quite 95%.  The 
##      problem is that a t-distribution is appropriate when
##      using the sample standard deviation.  Repeat part 2(b),
##      this time using t* in place of 1.96 in the formula,
##      where: t* = 2.262 for n = 10.

ct = 0  # counter for successes
n = 10 # the sample size
p = np.mean(p1)  # The true mean our population
for i in range(10000):
    s = np.random.choice(p1, size=10) # Generate a random sample
    xbar = np.mean(s)  # compute sample mean
    lcl = xbar - 2.262*np.std(s, ddof=1)/np.sqrt(n) # lower conf. limit
    ucl = xbar + 2.262*np.std(s, ddof=1)/np.sqrt(n)# upper conf. limit
    if lcl <= p and ucl >= p:
        ct += 1
ct/10000

"""
2c

0.9507               ##percentage in decimal form
95.07                   ##answer in percentage form
"""

## 3.   Suppose that random numbers are selected one at a time
##      with replacement from among the set 0, 1, 2, ..., 8, 9.
##      Use 10,000 simulations to estimate the average number 
##      of values required to select three identical values in 
##      a row.


ctarray = np.zeros(10000)  # An array to hold the values of ct
for i in range(10000):           ##for loop to simulate 10000 times
    list=[]                   ##makes an empty list to append the random values a,b, and c
    ct = 0  # Initialize the counter
    a = np.random.choice(range(10), size=1)         # initial random choices a, b, and c
    list.append(a)                                   ##adds values of a,b, and c to the list
    b = np.random.choice(range(10), size=1)
    list.append(b)
    c = np.random.choice(range(10), size=1)
    list.append(c)
    while list[ct]!=list[ct+1] or list[ct+1] !=list[ct+2]:       ##conditional code. If the three values are
        d = np.random.choice(range(10),size=1)      ##not equal to each other, then new value d will be added
        list.append(d)                                    ## to the list to compare to the pre-existing values
        ct +=1
    ctarray[i] = ct  # Record the number of selections required
np.mean(ctarray)  


"""
3

108.3428          ##avg number of values required to select three identical values in a row
"""

## 4.   Jay is taking a 20 question true/false quiz online.  The
##      quiz is configured to tell him whether he gets a question
##      correct before proceeding to the next question.  The 
##      responses influence Jay's confidence level and hence his 
##      exam performance.  In this problem we will use simulation
##      to estimate Jay's average score based on a simple model.
##      We make the following assumptions:
##    
##      * At the start of the quiz there is a 80% chance that 
##        Jay will answer the first question correctly.
##      * For all questions after the first one, if Jay got 
##        the previous question correct, then there is a
##        88% chance that he will get the next question
##        correct.  (And a 12% chance he gets it wrong.)
##      * For all questions after the first one, if Jay got
##        the previous question wrong, then there is a
##        70% chance that he will get the next question
##        correct.  (And a 30% chance he gets it wrong.)
##      * Each question is worth 5 points.
##
##      Use 10,000 simulated quizzes to estimate the average 
##      score.
ctarray = 10000*[0]
for i in range(10000):
    correct = 0         ##counts how many answers were correct
    for questions in range(20):     ## makes the quiz consisting of 20 questions
        if questions == 0:          ##check the condition when it's the first question
            points = np.random.choice([1,0], size=1, p=[.8,.2])       ## when answer is correct then
            correct = correct + points                                ## 1 is produced, if wrong then 0. 
        else:       ##used for questions after the first question
            if points == 1:       ## makes the probability condition for getting the first question correct
                points = np.random.choice([1,0], size=1, p=[.88,.12])
                correct = correct+points                 ##correct = correct+____correct used to sum up the points
            else:       ##makes the probability condition for getting 1st question wrong as well as getting other question wrong
                points = np.random.choice([1,0],size=1,p=[.7,.3])
                correct = correct + points
    ctarray[i] = correct
totalscore = np.mean(ctarray)*5         ##multiplies the number of correct questions by 5 to get the score
print(totalscore)

"""
4

85.03999999999999        ##average score of 10000 simulated quizzes
"""



## 5.   The questions in this problem should be done without the 
##      use of loops.  They can be done with NumPy functions.
##      The different parts use the array defined below.

import numpy as np # Load NumPy
arr1 = np.array([[2,5,7,0,2,5,-6,8,1,-9],[-1,3,4,2,0,1,3,2,1,-1],
                [3,0,-2,-2,5,4,5,9,0,7],[1,3,2,0,4,5,1,9,8,6],
                [1,1,0,1,5,3,2,9,0,-9],[0,1,7,7,7,-4,0,2,5,-9]])

## 5(a) Extract a submatrix arr1_slice1 from arr1 that consists of
##      the second and third rows of arr1.

arr_slice1 = np.copy(arr1[1:3])     ##slices arr1 to get 2nd and 3rd rows
    
"""
5a
array([[-1,  3,  4,  2,  0,  1,  3,  2,  1, -1],
       [ 3,  0, -2, -2,  5,  4,  5,  9,  0,  7]])
"""

## 5(b) Find a one-dimensional array that contains the entries of
##      arr1 that are less than -2.
arr1[arr1 < -2]         ##finds 1-d array that contains entries of arr1 < -2

"""
5b
array([-6, -9, -9, -4, -9])
"""

## 5(c) Determine the number of entries of arr1 that are greater
##      than 4.
np.sum((arr1 > 4))      ##adds the number of entries in arr1 > 4

"""
5c

18
"""

## 5(d) Find the mean of the entries of arr1 that are less than
##      or equal to -2.
np.mean(arr1[arr1 <= -2])       ## finds the mean of entries of arr1 <= -2

"""
5d

-5.857142857142857
"""


## 5(e) Find the sum of the squares of the odd entries of arr1.
np.sum(arr1[arr1%2 !=0]**2)             ### np.sum used to sum up all the squared values in the array
"""
5e

962
"""

## 5(f) Determine the proportion of positive entries of arr1 
##      that are greater than 5.
np.sum((arr1 > 5))/np.sum((arr1 > 0))*100       ## divides the number of arr1> 5 by the number of arr1 >0
                                                ## multiplied by 100 to get the proportion in % form

"""
5f

26.190476190476193  ## proportion in percentage
0.26190476190476193 ## proportion in decimals
"""

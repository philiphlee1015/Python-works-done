##  The questions in this assignment refer to the data in the
##  file 'absent.csv'.  The data contains 740 records from an
##  employer, with 21 columns of data for each record.  (There
##  are a few missing values indicated by zeros where zeros 
##  are clearly not appropriate.)  The file 'absent.pdf' has
##  a summary of the meanings for the variables.

##  Questions 1 and 2 can be completed without loops.  You should
##  try to do them this way, grading will take this into account.

## 1.  All questions refer to the data set 'absent.csv'.

## 1(a) Find the mean absent time among all records.
import numpy as np # load "numpy"
import pandas as pd # load pandas as pd
absent = pd.read_csv('absent.csv') # imports absent.csv

np.mean(absent)['Absenteeism time in hours']       ## finds the mean of the column labeled "Absenteeism time in hours"

"""
1a

6.924324324324324     ## mean absent time among all records.
"""

## 1(b) Determine the number of records corresponding to
##      being absent on a Thursday.
group1 = absent['Day of the week']==5    ## isolates the column with day of the week and if makes it display
                                           ##TRUE if the day == 5, which is Thursday
np.sum(group1)          ##counts how many number of TRUE is present to get number of records corresponding to 
                          ##being absent on a Thursday
"""
1b

125        ##number of records corresponding to Thursday
"""                      

## 1(c) Find the number of different employees represented in 
##      this data.

group2 = absent.groupby('ID')      ## isolates the data by ID
unique=group2.count()      ##counts how many of the IDs correspond to the number of data recorded, each row
                            ##corresponds to each unique IDs
len(unique)      ##finds the number of rows in unique

"""
1c

36
"""

## 1(d) Find the transportation expense for the employee with
##      ID = 34.
absent.loc[absent['ID']==34,'Transportation expense']     ##finds the transportation expenses related to the ID = 34
"""
1d

118      ##transportiation expense for the employee with ID=34
"""


## 1(e) Find the mean number of hours absent for the records
##      for employee ID = 11.
group1 = absent['Absenteeism time in hours'].groupby(absent['ID'])##groups data in column 'Absenteeism time in hours'
                                                         ## by 'ID' Column
group1.mean().loc[11]  ##finds the mean of absent hours and locates ID 11 and displays data corresponding to the ID

"""
1e

11.25               ##mean # of hrs absent for emplyee ID = 11
"""


## 1(f) Find the mean number of hours absent for the records of those who 
##      have no pets, then do the same for those who have more than one pet.
np.mean(absent.loc[absent['Pet']==0,'Absenteeism time in hours']) ##finds the mean of absent hours for those without pets by using .loc function
np.mean(absent.loc[absent['Pet']>1,'Absenteeism time in hours']) ##finds the mean of absent hours for those with more than 1 pets

"""
1f

6.828260869565217        ##mean absent hrs for those without pets
5.21830985915493         ## mean absent hrs for those with >1 pet
"""

## 1(g) Find the percentage of smokers among the records for absences that
##      exceeded 8 hours, then do the same for absences of no more then 4 hours.

group1=absent.loc[absent['Absenteeism time in hours']>8,['Social smoker']] ## isolates data by record with absent hours >8
len(group1.loc[group1['Social smoker']==1])/len(group1)*100 ##finds the number of smokers and divide by total number of people w/ more than 8 hrs of absence

group2=absent.loc[absent['Absenteeism time in hours']<=4,['Social smoker']]  ## isolates data by record with absent hours <=4
len(group2.loc[group2['Social smoker']==1])/len(group2)*100 ##finds the number of smokers and divide by total number of people w/ at most 4 hrs of absence

"""
1g

6.349206349206349 ##percentage of smokers among the records for absences that exceeds 8 hrs
6.29067245119306 ##percentage of smokers among the records for absences of no more than 4 hrs
"""

## 1(h) Repeat 1(g), this time for social drinkers in place of smokers.

group1=absent.loc[absent['Absenteeism time in hours']>8,['ID','Social drinker']] ## isolates data by record with absent hours >8
len(group1.loc[group1['Social drinker']==1])/len(group1)*100 ##finds the number of drinkers and divide by total number of people w/ more than 8 hrs of absence
 
group2=absent.loc[absent['Absenteeism time in hours']<=4,['ID','Social drinker']]  ## isolates data by record with absent hours <=4
len(group2.loc[group2['Social drinker']==1])/len(group2)*100 ##finds the number of drinkers and divide by total number of people w/ at most 4 hrs of absence

"""
1h

73.01587301587301 ## percentage of drinkers absnt hrs >8
53.36225596529284  ##percentage of drinkers absnt hrs <=4
"""

## 2.  All questions refer to the data set 'absent.csv'.

## 2(a) Find the top-5 employee IDs in terms of total hours absent.  List
##      the IDs and corresponding total hours absent.
group1 = absent['Absenteeism time in hours'].groupby(absent['ID'])     ##groups absent data by ID and absent hrs
tothrs=group1.sum()      ##finds the total absent hrs for each ID
tothrs.sort_values(ascending=False)[0:5,]   ##sorts the ID by absent hrs and displays the top-5 IDs with their hrs

"""
2a      ##left indicates ID, right indicates total hrs absent

ID
3     482
14    476
11    450
28    347
34    344
"""


## 2(b) Find the average hours absent per record for each day of the week.
##      Print out the day number and average.
group1 = absent['Absenteeism time in hours'].groupby(absent['Day of the week']) ##groups by asnt hrs and day of the wk
group1.mean() ##finds the mean for each day

"""
2b      ##left indicates day of absence, right indicates mean absent hrs

Day of the week
2    9.248447
3    7.980519
4    7.147436
5    4.424000
6    5.125000
"""

## 2(c) Repeat 2(b) replacing day of the week with month.
group1 = absent['Absenteeism time in hours'].groupby(absent['Month of absence']) ##groups by asnt hrs and Month of absence
group1.mean() ##finds the mean for each month

"""
2c           ##left indicates month of absence, right indicates mean absent hrs
Month of absence
1      4.440000
2      4.083333
3      8.793103
4      9.094340
5      6.250000
6      7.611111
7     10.955224
8      5.333333
9      5.509434
10     4.915493
11     7.507937
12     8.448980
"""

## 2(d) Find the top 3 most common reasons for absence for the social smokers,  
##      then do the same for the non-smokers. (If there is a tie for 3rd place,
##      include all that tied for that position.)
group1 = absent.loc[absent['Social smoker']==1,['Reason for absence']]  ##isolates the data by social smoker and reason for absence
frequency=group1['Reason for absence'].value_counts() ##counts how many times the reason has been used
frequency[1:9]    ##displays the top 3 common reasons for smokers

group2 = absent.loc[absent['Social smoker']==0,['Reason for absence']] ##same as the top codes but for non-smokers
frequency2=group2['Reason for absence'].value_counts() ##counts how many times the reason has been used
frequency2[0:3]    ##displays the top 3 common reasons for non-smokers


"""
2d      ##left indicates reason for absence, right indicates number of times that the reason had been used
            ##there were 5 ties for the 2nd position and 2 ties for 3rd position
           ##top data is for smokers, bottom data below ---- line is for non-smokers
25    7
19    4
18    4
28    4
22    4
23    4
14    3
11    3
---------
23    145
28    108
27     69
"""
## 2(e) Suppose that we consider our data set as a sample from a much
##      larger population.  Find a 95% confidence interval for the 
##      proportion of the records that are from social drinkers.  Use
##      the formula 
##
##  [phat - 1.96*sqrt(phat*(1-phat)/n), phat + 1.96*sqrt(phat*(1-phat)/n)]
##
## where "phat" is the sample proportion and "n" is the sample size.

drink=absent.loc[absent['Social drinker']==1]        ##isolates the data by social drinkers
n = len(absent) # the total sample size          
phat = len(drink)/n   # compute sample proportion by dividing the number of social drinker records by total number of records
lcl = phat - 1.96*np.sqrt(phat*(1-phat)/n) # lower conf. limit
ucl = phat + 1.96*np.sqrt(phat*(1-phat)/n) # upper conf. limit
print(lcl,ucl)

"""
2e  ##displays 95% confidence interval

0.5318725067607831 0.603262628374352
"""

## 3.  For this problem we return to simulations one more time.  Our
##     topic is "bias" of estimators, more specifically the "percentage
##     relative bias" (PRB) which we take to be
##
##        100*((mean of estimated values) - (exact value))/(exact value)
##
##     For instance, to approximate the bias of the sample mean in 
##     estimating the population mean, we would computer
##
##        100*((mean of sample means) - (population mean))/(population mean)
##
##     For estimators that are "unbiased" we expect that the average
##     value of all the estimates will be close to the value of the
##     quantity being estimated.  In these problems we will approximate
##     the degree of bias (or lack of) by simulating.  In all parts we
##     will be sampling from a population of 10,000,000 values randomly
##     generated from an exponential distribution with scale = 10 using
##     the code below.

pop = np.random.exponential(scale = 10, size = 10000000)

## 3(a) Compute and report the mean for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample mean for each of the samples,
##      compute the mean of the sample means, and then compute the PRB.

popmean=np.mean(pop) ## calculates the mean for all of "pop"
list=[]       ##makes an empty list to contain sample means
for i in range(100000):      ##simulate 100000 samples of size 10 from population, calculates mean of the samples, and adds the means to the list created above
    samp=np.random.choice(pop,size=10)
    samps=np.mean(samp)
    list.append(samps)     ##adds sample mean to the list
meansamplemeans=np.mean(list) ## finds the mean of the sample means

prb=100*((meansamplemeans-popmean))/popmean ##calculates the PRB
print(prb)


"""
3a

10.00075794208763     ## mean for all of "pop"
-0.031949384025169135 ## PRB value

"""

## 3(b) Compute and report the variance for all of "pop" using "np.var(pop)".  
##      Simulate 100,000 samples of size 10, then compute the sample variance 
##      for each sample using "np.var(samp)" (where "samp" = sample).  Compute 
##      the mean of the sample variances, and then compute the PRB.
##      Note: Here we are using the population variance formula on the samples
##      in order to estimate the population variance.  This should produce
##      bias, so expect something nonzero for the PRB.

popvar = np.var(pop)   ##calculates variance for all of "pop"
list=[]       ##makes an empty list to add 100000 sample var means
for i in range(100000):            ##same as code in 3a except that it's calculating for sample variance
    samp3b=np.random.choice(pop,size=10)
    samp3bvar=np.var(samp3b)
    varmean=np.mean(samp3bvar)
    list.append(varmean)

 
listmeans=np.mean(list)   ##finds the mean of sample variance means
prb3b=100*((listmeans-popvar))/popvar     ##calculates the PRB
print(prb3b)
"""
3b

100.11531896584832 ##variance for all of "pop"
-9.253052719527618  ##PRB
"""


## 3(c) Repeat 3(b), but this time use "np.var(samp, ddof=1)" to compute the
##      sample variances.  (Don't change "np.var(pop)" when computing the
##      population variance.)
popvar = np.var(pop)   ##calculates variance for all of "pop"
list=[]       ##makes an empty list to add 100000 sample var means
for i in range(100000):            ##same as 3b except that sample variance is calculated using ddof=1
    samp3c=np.random.choice(pop,size=10)
    samp3cvar=np.var(samp3c,ddof=1)
    varmean=np.mean(samp3cvar)
    list.append(varmean)


listmeans=np.mean(list)      ##finds the mean of sample variance means
prb3c=100*((listmeans-popvar))/popvar        ##calculates the PRB
print(prb3c)     

"""
3c

100.11531896584832     ## population variance
-0.35144071840083885 ## PRB
"""


## 3(d) Compute and report the median for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample median for each of the samples,
##      compute the mean of the sample medians, and then compute the PRB.
##      Note: For nonsymmetric distributions (such as the exponential) the
##      sample median is a biased estimator for the population median.  The
##      bias gets decreases with larger samples, but should be evident with 
##      samples of size 10.
popmed=np.median(pop)  ## calculates the median for all of "pop"
list=[]       ##makes an empty list to contain sample means of medians
for i in range(100000):      ##simulate 100000 samples of size 10 from population, calculates median of the samples, and adds the medians to the list created above
    samp=np.random.choice(pop,size=10)
    samps=np.median(samp)
    list.append(samps)     ##adds sample medians to the list
meansamplemeds=np.mean(list) ## finds the mean of the sample medians

prb=100*((meansamplemeds-popmed))/popmed ##calculates the PRB
print(prb)



"""
3d

6.927918839338053 ## population median
7.458903178562381 ## PRB
"""
